from __future__ import unicode_literals
import json
from django.db import models
from django.http import JsonResponse


class Location(models.Model):
    location_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.location_name
   
class Connection(models.Model):
    base= models.CharField(max_length=200)	
    location = models.ForeignKey(Location)
    ip = models.CharField(max_length=200)
    port = models.IntegerField(default=0)
    mfdbname= models.CharField(max_length=200)
    bfdbname= models.CharField(max_length=200)

    def __str__(self):
        return self.ip
