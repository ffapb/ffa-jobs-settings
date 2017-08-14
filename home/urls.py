from django.conf.urls import url

# https://stackoverflow.com/a/14379897/4126114
from django.views.generic import TemplateView

app_name='home'
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home/index.html'), name='index')
]


