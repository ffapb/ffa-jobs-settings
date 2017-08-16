
It's a Web app:
- To set emails for each cron job
- For switching the system database server from a location to other one 
# Installation
Check Dockerfile

# Docker

Build locally: `docker build . -t minerva22/ffa-jobs-emails:local`

Download from [hub.docker.com](https://hub.docker.com/r/minerva22/ffa-jobs-emails/): `docker run -it -p 8000:8000 minerva22/ffa-jobs-emails`

After `up`, run `createsuperuser`: `> docker-compose exec jobs_emails pew in FFA_JOBS_EMAILS python manage.py createsuperuser`

Copy database file from local server to docker container:
```
> docker ps|grep jobs_emails
3b94119bfb68        minerva22/ffa-jobs-emails ...
> docker cp ~/db.sqlite3 3b94119bfb68:/usr/share/ffa-jobs-emails/
```


