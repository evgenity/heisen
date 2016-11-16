from django.shortcuts import render_to_response, render, redirect
from django.contrib import auth
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

def profile(request,slack_id):
    if request.method == 'GET':
        person = Person.objects.get(slack_id=slack_id)
        template_name = 'home/profile.html'
        if request.user.is_authenticated:
            if person.slack_id==request.user.person.slack_id or request.user.is_staff:
                return render(request,template_name,context={'person':person,'tags':Tag.objects.all()})
            else:
                return redirect('/team')
        else:
            return redirect('/team')
    elif request.method == 'POST':
        person = Person.objects.get(slack_id=slack_id)
        if request.user.is_staff:
            tag=Tag.objects.get(name=request.POST['tag'])
            tag.persons.add(person)
            tag.save()
        template_name = 'home/profile.html'
        return render(request,template_name,context={'person':person,'tags':Tag.objects.all()})

    person = Person.objects.get(slack_id=slack_id)
    template_name = 'home/profile.html'
    return render(request,template_name,context={'person':person,'tags':Tag.objects.all()})
