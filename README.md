#Fix issue: django.db.utils.IntegrityError: NOT NULL constraint failed:
	
# create a Python virtual environment by typing:

virtualenv myprojectenv


	Run: - python manage.py makemigrations 
             - python manage.py sqlmigrate 
             - python manage.py migrate

# Ordering in Selecting Objects in Django Model -(example by job_text)
# add in view.py 

	def get_queryset(self):
        """Return the  jobs by order alphabetic."""
        return Job.objects.order_by('job_text')



# Ordering the display items alphabetically in Django-Admin
# add in admin.py

	class JobAdmin(admin.ModelAdmin): 
  		list_display = ('job_text', 'pub_date')
  		ordering = ('job_text',) # The negative sign indicate descendent order
 
	admin.site.register(Job,JobAdmin)



# Edit your emailffa/admin.py file again and add an improvement to the Job change list page: 

filters using the list_filter. Add the following line to JobAdmin:

	list_filter = ['pub_date']


# Pagination example 
 https://ana-balica.github.io/2015/01/29/pagination-in-django/
# Remove directory from remote repository after adding them to .gitignore
 - git rm -r --cached . 
 - git add .
 - git commit -m 'Removed all files that are in the .gitignore' 
 - git push origin master


# Use the "ours" merge strategy to overwrite master with other branch like temp  

 - git checkout temp
 - git merge -s ours master
 - git checkout master
 - git merge temp



# How to return JsonResponse in Django generic ListView
https://stackoverflow.com/questions/39768671/how-to-return-jsonresponse-in-django-generic-listview
	def get(self, *args, **kwargs):
    	queryset = self.get_queryset()
        data = serializers.serialize("json", queryset)
        return JsonResponse(data, safe=False)


# Docker

Build locally: `docker build . -t minerva22/ffa-jobs-emails:local`

Download from [hub.docker.com](https://hub.docker.com/r/minerva22/ffa-jobs-emails/): `docker run -it -p 8000:8000 minerva22/ffa-jobs-emails`

After `up`, run `createsuperuser`: `> docker-compose exec jobs_emails pew in FFA_JOBS_EMAILS python manage.py createsuperuser`

Copy database file from local server to docker container:
```
> docker ps|grep jobs_emails
3b94119bfb68        minerva22/ffa-jobs-emails ...
> docker cp ~/db.sqlite3 3b94119bfb68:/usr/share/ffa-jobs-emails/
```

# How to Filter QuerySets Dynamically
 - pip install django-filter
 - Create a file named filters.py inside your app folder

 class UserFilter(django_filters.FilterSet):
    class Meta:
        model = Job
        fields = ['id', 'job_text', ' ]

 - In views.py add a search function:

https://simpleisbetterthancomplex.com/tutorial/2016/11/28/how-to-filter-querysets-dynamically.html

install:
pip install django-filter

def search(request):
    job_list = Job.objects.all()
    job_filter = JobFilter(request.GET, queryset=job_list)
    return render(request, 'emailffa/job_list.html', {'filter': job_filter})


  - The a route in urls.py:
 url(r'^search/$', views.search, name='search'),


 - Finally, create a html file in templates 'job_list.html':

{% block content %}
  <form method="get">
    {{ filter.form.as_p }}
    <button type="submit">Search</button> 
  
  
  <ul>
  {% for job in filter.qs %}
    <li> {{ job.id }}-{{ job.job_text }} </li>
  {% endfor %}
  </ul>
{% endblock %} 

</form>
 <a href="{% url 'emailffa:search' %}">
   <button>Reset</button>
</a>




