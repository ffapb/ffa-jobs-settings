#!/bin/sh

if [ -z "$NATS_URI" ]; then
  echo "Env var NATS_URI not defined. Aborting."
  exit 1
fi

# drop the lock file
rm -rf $SIC_UPDATE_LOCK

# launch django server
# ATM using the dev built-in server .. will move later to nginx maybe
pew in FFA_ES_SPLITTER python3 manage.py migrate
# pew in FFA_ES_SPLITTER python3 manage.py createsuperuser --no-input --username admin

# launch syslog
syslogd

# run server
pew in FFA_ES_SPLITTER  python3 manage.py runserver 0.0.0.0:8000 | logger -t "runserver" &

#----------------------------------
# Listen on nats channel fscrawler for updates from fscrawler (i.e. new files) and run my django admin command
# Note that the nats sub below for docker-update.sh is the same as that in the cron job further below
# except for the "nats pub" part which is unnecessary except for user-triggered updates, i.e. for file uploads by the user
#
# EDIT 2017-05-30: since the user now uploads the file directly from the django ui, and not by placing a copy in a folder,
#                  the django app itself can trigger the splitter command upon file upload (without the importMarketflow).
#                  This means that the below nats sub can be removed.
#                  It would allow me to complete the test sic-namecheck.search.tests.DocNewTests.test_post_live
#                  such that it ends up with "File uploaded successfully", instead of having to stop at "splitting still in progress",
#                  which would have been the case had the splitting still depended on the nats sub below.
#                  The decision is purely test-driven to be able to test the workflow more completely from the sic-namecheck tests.
#                  I realize that the test is an integration test and not a unit test, and that such a test would be more suitable
#                  to be done in docker-sic-namecheck, but ... whatever
#
# EDIT 2017-06-02:
# so ... bummer ... the splitter command in docker-update.sh was too slow.
# I split it into a splitter and a search. It was the search that was really slow because it had to loop over all entities.
# As such, I went back to the nats call below, and I moved the embedded nats reply in between the splitter and the search.
# This way, the user upload could return (relatively quickly) after the splitter (which creates the document in django).
# Later refreshes of the document list would display the status of the slower "search"
nats \
  --server "$NATS_URI" \
  sub \
  --cmd "docker-update.sh splitter 2>&1 | logger -t splitter" \
  --token "fscrawler done" \
  "namecheck" 2>&1 | logger -t "nats" &
#  --print
#----------------------------------

# save to cron, launch
# note that cron job below for docker-update.sh is the same as that in the nats sub command above
echo "*/15 * * * * (docker-update.sh importMarketflow 2>&1 && curl -fsS --retry 3 $HCHK_UPDATE > /dev/null) | logger -t importMarketflow" >> /etc/crontabs/root
echo "0 0 * * * (docker-backup.sh && curl -fsS --retry 3 $HCHK_BACKUP > /dev/null) | logger -t backup" >> /etc/crontabs/root

crond -b

# wait 1 second for the cron above to send its start output to syslog
sleep 1 

# tail the logs
tail -f /var/log/messages
