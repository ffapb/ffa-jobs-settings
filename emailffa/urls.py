from django.conf.urls import url,include

from . import views

app_name='emailffa'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^results/$', views.SearchView, name='results'),
   # url(r'^', include('emailffa.search.views.results')),
   
    
]


