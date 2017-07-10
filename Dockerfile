FROM python:alpine
RUN apk --update add git gcc musl-dev 
RUN pip3 install pew
RUN pew new FFA_JOBS_EMAILS

# pymssql on separate line because it's such a pain
# also, can't just use pymssql until https://github.com/pymssql/pymssql/issues/432#issuecomment-238257092
RUN pew in FFA_JOBS_EMAILS pip3 install Django


# for queryset filter in openCasesSameDate
RUN pew in FFA_ES_SPLITTER pip install pytz

# pagination
# remove "==1.2" when this is closed: https://github.com/staticdev/django-pagination-bootstrap/issues/27
# and this as well: https://github.com/staticdev/django-pagination-bootstrap/issues/28
RUN pew in FFA_ES_SPLITTER pip install django-pagination-bootstrap==1.2

# for the doc upload from the django app
RUN pew in FFA_ES_SPLITTER pip install requests

# check note about nats above
RUN pew in FFA_ES_SPLITTER pip install asyncio-nats-client

# dev note: can move this to earlier 'apk add'
RUN apk --update add curl

RUN  mkdir -p /var/lib/sic-namecheck/ \
  && mkdir -p /var/lib/sic-namecheck/backups \
  && mkdir -p /var/lib/sic-namecheck/db \
  && mkdir -p /var/lib/sic-namecheck/docs

VOLUME /var/lib/sic-namecheck

EXPOSE 8000
WORKDIR /usr/share/sic-namecheck
COPY sic-namecheck/ .

COPY docker-entry.sh /usr/bin/
RUN chmod +x /usr/bin/docker-entry.sh
COPY docker-update.sh /usr/bin/
RUN chmod +x /usr/bin/docker-update.sh
COPY docker-backup.sh /usr/bin/
RUN chmod +x /usr/bin/docker-backup.sh

ENV SIC_UPDATE_LOCK /var/lib/sic-namecheck/update.lock

ENTRYPOINT docker-entry.sh
