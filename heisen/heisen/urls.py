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
from home import views as home_views
from heisen import settings
from django.conf.urls.static import static
from django.conf.urls import (
handler400, handler403, handler404, handler500
)

handler500 = 'heisen.views.server_error'
handler404 = 'heisen.views.page_not_found'
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^partners/', include('partners.urls')),
    #url(r'^projects/', include('projects.urls')),
    url(r'^tasks/', include('tasks.urls')),
    url(r'^team/', include('team.urls')),
    url(r'^$', include('home.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^logout$',views.logout,name='logout'),
    url(r'^robots.txt$',home_views.robots,name='robots'),
    url(r'^sitemap.xml$',home_views.sitemap,name='sitemap'),
    url(r'^profile/(?P<slack_id>[\w-]+)',home_views.profile,name='profile'),
    url(r'^contacts/',home_views.contacts,name='contacts'),
    url(r'^blog/', include('zinnia.urls')),
    url(r'^django-rq/', include('django_rq.urls')),
#    url(r'^complete/slack$', views.loggedin, name='index'),
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
