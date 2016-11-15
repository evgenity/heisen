from django.conf.urls import url

from . import views

app_name = 'team'
urlpatterns = [
    url(r'^$', views.TeamView, name='index'),
    url(r'^filter$', views.Filter, name='filter'),
    url(r'^tags$', views.Tags, name='tags'),
]
