import json
from django.core import serializers
from django.views import generic
from django.http import JsonResponse
import operator
from .models import Job
#from .models import Email
#from .models import Cron
#from django.contrib import auth




class IndexView(generic.ListView):
    template_name = 'emailffa/index.html'
    context_object_name = 'latest_job_list'
    model= Job
    paginate_by = 15

    def get_queryset(self):
        """Return the  jobs by order alphabetic."""
        return Job.objects.order_by('id')

    def get(self, *args, **kwargs):
        asjson = self.request.GET.get('asjson', "false")
        asjson=asjson.lower()=="true"
          
        if not asjson:
            return super(IndexView, self).get(*args, **kwargs)
        #https://stackoverflow.com/questions/39768671/how-to-return-jsonresponse-in-django-generic-listview
        
        #queryset = self.get_queryset()
        #data = serializers.serialize("json", queryset) -- Get all data from queryset
        
        #Get a specific fileds from queryset
        #https://docs.djangoproject.com/en/1.7/topics/serialization/
        
        data = [{"job_id": job.id, "job_text": job.job_text} for job in Job.objects.all()]
        
        return JsonResponse(data,safe=False)

class SearchView(generic.ListView):
    
   
    def search(request):
    	
    	query = request.GET['q']
    	t = loader.get_template('templates/results.html')
   	c = Context({ 'query': query,})
    	return HttpResponse(t.render(c))


class DetailView(generic.DetailView):
      model = Job
      template_name = 'emailffa/detail.html'


      def get(self, *args, **kwargs):

          #url="http://localhost:8000/emailffa/1/?asjson=true"
       
          #http://programtalk.com/vs2/python/2464/django-completion/completion/views.py/
          asjson = self.request.GET.get('asjson', "false")
          asjson=asjson.lower()=="true"
          
          if not asjson:
              return super(DetailView, self).get(*args, **kwargs)

          #https://stackoverflow.com/questions/34460708/checkoutview-object-has-no-attribute-object
          self.object = self.get_object()
          context = super(DetailView, self).get_context_data(**kwargs)
          job = context["job"]
          output = {
            "job_id": job.id,
            "job_text": job.job_text,
            "pub_date": job.pub_date.strftime("%Y-%m-%d"),
            "job_cron": job.job_cron,
            "email_set": [x.email_text for x in job.email_set.all()]
          }
          return JsonResponse(output)


#def detail(request, job_id):
    #job = get_object_or_404(Job, pk=job_id)
    #return render(request, 'emailffa/detail.html', {'job': job})


