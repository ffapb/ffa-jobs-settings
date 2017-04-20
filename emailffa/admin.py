from django.contrib import admin

# Register your models here.
from .models import Job
from .models import Email

admin.site.register(Job)
admin.site.register(Email)
