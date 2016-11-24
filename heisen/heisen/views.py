from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from form import RegistrationForm
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from django.template import RequestContext

from team.models import Person
from home.cron import update_team

#404 Error
def page_not_found(request):
    response = render_to_response(
    '404.html',
    #context_instance=RequestContext(request)
    )

    response.status_code = 404

    return response
#500 Error
def server_error(request):
    response = render_to_response(
    '500.html',
    #context_instance=RequestContext(request)
    )
    response.status_code = 500
    return response

def bind_user(backend, user, response, *args, **kwargs):
    if backend.name == 'slack':
        print(user.username.split("@")[0])
        try:
            person=Person.objects.get(slack_name=user.username.split("@")[0])
        except ObjectDoesNotExist:
            person=update_team(break_user=user.username.split("@")[0])
        person.user=user
        person.save()

def loggedin(request):
    return redirect('/')

def logout(request):
    auth.logout(request)
    return redirect('/')
