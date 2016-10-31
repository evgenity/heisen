from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from form import RegistrationForm
from django.contrib import auth

from team.models import Person

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            person=Person.objects.get(slack_name=form.cleaned_data['slack_name'])
            person.user=user
            person.save()
            print user.person.full_name
            return HttpResponseRedirect('/accounts/register/complete')

    else:
        form = RegistrationForm()
    return render(request,'registration/registration_form.html',context={'form':form})

def registration_complete(request):
    return render(request,'registration/registration_complete.html')

def login(request):
    return render(request,'registration/login.html')

def process_login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/login_error')

def loggedin(request):
    return render(request,'registration/loggedin.html',
                              {'username': request.user.username})

def login_error(request):
    return render(request,'registration/login_error.html')

def logout(request):
    auth.logout(request)
    return render(request,'registration/logged_out.html')
