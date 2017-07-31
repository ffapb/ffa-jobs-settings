from django.db import models

import datetime
from django.utils import timezone
from django.db import models
from django.utils.encoding import python_2_unicode_compatible





class Tag(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Job(models.Model):
    job_text = models.CharField(max_length=255, unique=True)
    pub_date = models.DateTimeField('date published')
    job_cron=models.CharField(max_length=200)
    tag = models.ManyToManyField(Tag)


    def __str__(self):
        return self.job_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

   
 
class Email(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    email_text = models.CharField(max_length=200)
    

    def __str__(self):
        return self.email_text

#class Cron(models.Model):
 #   job = models.ForeignKey(Job, on_delete=models.CASCADE)
   # cron_text = models.CharField(max_length=200)
    

    #def __str__(self):
     #   return self.cron_text


