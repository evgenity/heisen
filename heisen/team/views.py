from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse

from team.models import Person,Tag
from tasks.models import Progress


class IndexView(generic.ListView):
    template_name = 'team/index.html'
    context_object_name = 'team_list'
    def get_queryset(self):
        return Person.objects.all().order_by('-avatar','-progress__rating')

def TeamView(request):
    template_name = 'team/index.html'
    return render(request,template_name)

def Tags(requst):
    return JsonResponse([tag.name for tag in Tag.objects.all()],safe=False)

def Filter(request):
    team_list = Person.objects.all().order_by('-avatar','-progress__rating')
    tl = []
    for person in team_list:
        if person.first_name:
            name = person.first_name
        else:
            name = person.slack_name[:7]+"..."
        skills=[]
        for tag in person.tags.all():
            skills.append(tag.name)
        tl.append({
            'name': name,
            'slack_id': person.slack_id,
            'avatar': person.slack_avatar,
            'skills': skills,
        })
    return JsonResponse(tl,safe=False)
