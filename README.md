
It's a Web app:
- To set emails for each cron job
- For switching the system database server from a location to other one:
	1. define connection information: ip, port, user, password, mf db name, bf db name
	2. define above information multiple times: for different locations


# Installation
Check Dockerfile

# Docker

Build locally: `docker build . -t ffapb/ffa-jobs-settings:local`

Download from [hub.docker.com](https://hub.docker.com/r/minerva22/ffa-jobs-emails/): `docker run -it -p 8000:8000 ffapb/ffa-jobs-settings`

After `up`, run `createsuperuser`: `> docker-compose exec jobs_emails pew in FFA_JOBS_SETTINGS python manage.py createsuperuser`

Copy database file from local server to docker container:
```
> docker ps|grep jobs_emails
3b94119bfb68        ffapb/ffa-jobs-settings ...
> docker cp ~/db.sqlite3 3b94119bfb68:/usr/share/ffa-jobs-emails/
```

# Developer notes
[DEVNOTES.md](DEVNOTES.md)
