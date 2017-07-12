#!/bin/sh

# launch django server
# ATM using the dev built-in server .. will move later to nginx maybe
pew in FFA_JOBS_EMAILS python manage.py migrate
# pew in FFA_ES_SPLITTER python manage.py createsuperuser --no-input --username admin

# launch syslog
syslogd

# run server
pew in FFA_JOBS_EMAILS  python manage.py runserver 0.0.0.0:8000 | logger -t "runserver" &

# wait 1 second for the cron above to send its start output to syslog
sleep 1 

# tail the logs
tail -f /var/log/messages
