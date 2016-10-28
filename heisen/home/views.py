from django.shortcuts import render_to_response, render
from django.contrib import auth
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    template_name = 'home/index.html'
    return render(request,template_name)



def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        data = request.POST.copy()
        errors = form.get_validation_errors(data)
        if not errors:
            #new_user = form.save(data)
            print data
            return HttpResponseRedirect("/")
    else:
        data, errors = {}, {}

    return render_to_response("registration/register.html", {
        'form' : forms.FormWrapper(form, data, errors)
    })
