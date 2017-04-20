from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.http import HttpResponse
from .models import Job
from .models import Email

def index(request):
    latest_job_list = Job.objects.order_by('-pub_date')
    template = loader.get_template('emailffa/index.html')
    context = {
        'latest_job_list': latest_job_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    return render(request, 'emailffa/detail.html', {'job': job})
