from __future__ import unicode_literals
import json
from django.db import models
from django.http import JsonResponse

from django import forms   

LOCATIONS_CHOICES = (
    ('beirut','BEIRUT'),
    ('bsalim', 'BSALIM'),
    ('test','TEST'),
    
)


class Location(models.Model):
  
   location_name = models.CharField(max_length=10, locations=LOCATIONS_CHOICES, default='beirut')
    
   def __str__(self):
        return self.location_name
   
class Connection(models.Model):
    base= models.CharField(max_length=200)	
    location = models.ForeignKey(Location)
    ip = models.CharField(max_length=200)
    port = models.CharField(max_length=200)
    mfdbname= models.CharField(max_length=200)
    bfdbname= models.CharField(max_length=200)
    user= models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return "%s:  %s"%(self.location, self.base)
