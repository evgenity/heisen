from django.conf.urls import url

from . import views

app_name = 'tasks'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^progress$', views.progress, name='progress'),
]
