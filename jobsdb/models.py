from __future__ import unicode_literals
import json
from django.db import models
from django.http import JsonResponse

from django import forms   




class Location(models.Model):
  
   location_name = models.CharField(max_length=10)
   isdefault=models.BooleanField(default=False)
    
   def __str__(self):
        return self.location_name
   
   def clean(self):
       if not self.isdefault: return 
       for l in Location.objects.all():
           l.isdefault= False
           l.save()
   
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
