from django.shortcuts import render_to_response, render
from django.contrib import auth
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect

from team.models import Person, Tag
from tasks.models import Progress
# Create your views here.
def index(request):
    template_name = 'home/index.html'
    return render(request,template_name)

def robots(request):
    template_name = 'home/robots.txt'
    return render(request,template_name)

def profile(request):
    person = Person.objects.get(user=request.user.id)
    template_name = 'home/profile.html'
    return render(request,template_name,context={'person':person})
