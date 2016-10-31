"""heisen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^partners/', include('partners.urls')),
    #url(r'^projects/', include('projects.urls')),
    url(r'^tasks/', include('tasks.urls')),
    url(r'^team/', include('team.urls')),
    url(r'^$', include('home.urls')),
    url(r'^accounts/register/$', views.register, name='register'),
    url(r'^accounts/register/complete/$', views.registration_complete, name='registration_complete'),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/process_login/$', views.process_login, name='process_login'),
    url(r'^accounts/loggedin/$', views.loggedin, name='loggedin'),
    url(r'^accounts/login_error/$', views.login_error, name='login_error'),
    url(r'^accounts/logout/$', views.logout, name='logout'),

    ]
