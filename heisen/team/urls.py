from django.conf.urls import url

from . import views

app_name = 'team'
urlpatterns = [
    url(r'^$', views.TeamView, name='index'),
    url(r'^2$', views.TeamView2, name='index2'),
    url(r'^filter$', views.Filter, name='filter'),
]
