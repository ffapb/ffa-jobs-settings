# Fix issue: django.db.utils.IntegrityError: NOT NULL constraint failed:
	
#create a Python virtual environment by typing:
virtualenv myprojectenv


	Run: - python manage.py makemigrations 
             - python manage.py sqlmigrate 
             - python manage.py migrate

# Ordering in Selecting Objects in Django Model -(example by job_text)
#add in view.py 

	def get_queryset(self):
        """Return the  jobs by order alphabetic."""
        return Job.objects.order_by('job_text')



# Ordering the display items alphabetically in Django-Admin
# add in admin.py

	class JobAdmin(admin.ModelAdmin): 
  		list_display = ('job_text', 'pub_date')
  		ordering = ('job_text',) # The negative sign indicate descendent order
 
	admin.site.register(Job,JobAdmin)



# Filters using the list_filter. 
Edit your emailffa/admin.py file again and add an improvement to the Job change list page:
Add the following line to JobAdmin:

	list_filter = ['pub_date']


# Pagination example https://ana-balica.github.io/2015/01/29/pagination-in-django/
