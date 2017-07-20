from .models import Job
import django_filters

class JobFilter(django_filters.FilterSet):
    class Meta:
        model = Job
        fields = ['job_text', 'id', ]
