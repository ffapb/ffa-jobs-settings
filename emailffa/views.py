from django.shortcuts import render
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
    return HttpResponse("You're looking at job %s." % job_id)
