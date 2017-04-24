from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Job
from .models import Email

class IndexView(generic.ListView):
    template_name = 'emailffa/index.html'
    context_object_name = 'latest_job_list'

    def get_queryset(self):
        """Return the  published jobs."""
        return Job.objects.order_by('-pub_date')

class DetailView(generic.DetailView):
      model = Job
      template_name = 'emailffa/detail.html'



def detail(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    return render(request, 'emailffa/detail.html', {'job': job})


