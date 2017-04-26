from django.contrib import admin

# Register your models here.
from .models import Job, Email

class JobAdmin(admin.ModelAdmin):  
  list_display = ('job_text', 'pub_date')
  ordering = ('job_text',) # The negative sign indicate descendent order
  list_filter = ['pub_date']
admin.site.register(Job,JobAdmin)
admin.site.register(Email)
