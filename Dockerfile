FROM python:alpine
RUN apk --update add git gcc musl-dev 
RUN pip3 install pew
RUN pew new FFA_JOBS_EMAILS

# pymssql on separate line because it's such a pain
# also, can't just use pymssql until https://github.com/pymssql/pymssql/issues/432#issuecomment-238257092
RUN pew in FFA_JOBS_EMAILS pip3 install Django


# for queryset filter in openCasesSameDate
RUN pew in FFA_JOBS_EMAILS pip install pytz

# pagination
# remove "==1.2" when this is closed: https://github.com/staticdev/django-pagination-bootstrap/issues/27
# and this as well: https://github.com/staticdev/django-pagination-bootstrap/issues/28
RUN pew in FFA_JOBS_EMAILS pip install django-pagination-bootstrap==1.2

# for the doc upload from the django app
RUN pew in FFA_JOBS_EMAILS pip install requests

# check note about nats above
RUN pew in FFA_JOBS_EMAILS pip install asyncio-nats-client

# dev note: can move this to earlier 'apk add'
RUN apk --update add curl



#VOLUME /var/lib/sic-namecheck

EXPOSE 8000
WORKDIR /usr/share/ffa-job-emails
COPY ffa-job-emails/ .

COPY docker-entry.sh /usr/bin/
RUN chmod +x /usr/bin/docker-entry.sh



ENTRYPOINT docker-entry.sh
