from django.db import models

import datetime
from django.utils import timezone
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


class Job(models.Model):
    job_text = models.CharField(max_length=255, unique=True)
    pub_date = models.DateTimeField('date published')
    job_text.alphabetic_filter = True

    def __str__(self):
        return self.job_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
 
class Email(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    email_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.email_text
