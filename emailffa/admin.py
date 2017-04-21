from django.contrib import admin

# Register your models here.
from .models import Job, Email





admin.site.register(Job)
admin.site.register(Email)
