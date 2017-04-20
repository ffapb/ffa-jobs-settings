from django.conf.urls import url

from . import views

app_name='emailffa'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^specifics/(?P<job_id>[0-9]+)/$', views.detail, name='detail'),
]
