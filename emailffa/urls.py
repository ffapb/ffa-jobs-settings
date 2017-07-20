from django.conf.urls import url,include

from django.contrib import admin
from . import views



app_name='emailffa'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^search/$', views.search, name='search'),
    #url(r'^results/$', include('emailffa.views.search')),
    

    
]


