from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from form import RegistrationForm
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist

from team.models import Person
from home.cron import update_team

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
    return render(request,'registration/logged_out.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
