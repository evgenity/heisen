from django.shortcuts import render
from django.contrib import auth
from django import forms

# Create your views here.
def index(request):
    template_name = 'home/index.html'
    return render(request,template_name)

class LoginForm(forms.Form):
    username = forms.CharField(label=u'name')
    password = forms.CharField(label=u'password', widget=forms.PasswordInput())

def log_in(request):
    if ('username' in request.REQUEST) and ('password' in request.REQUEST):
        username = request.REQUEST['username']
        password = request.REQUEST['password']
        user = authenticate(username=username, password=password)
        print(user)
    return render_to_response('login.html')
