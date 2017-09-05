from django import forms 
from django.db import models 
from models import Location


class LocationForm(forms.Form):
    class Meta:
        model = Location
        fields = ['location_name']
