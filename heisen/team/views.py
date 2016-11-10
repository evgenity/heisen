from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse

from team.models import Person,Tag,Level
from tasks.models import Progress


class IndexView(generic.ListView):
    template_name = 'team/index.html'
    context_object_name = 'team_list'
    def get_queryset(self):
        return Person.objects.all().order_by('-avatar','-progress__rating')

def TeamView(request):
    template_name = 'team/index.html'
    #context_object_name = 'team_list'
    team_list=list(Person.objects.all().order_by('-avatar','-progress__rating'))
    return render(request,template_name,context={'team_list':team_list} )

def TeamView2(request):
    template_name = 'team/index2.html'
    return render(request,template_name)

def Filter(request):
    team_list = Person.objects.all().order_by('-avatar','-progress__rating')
    # print "REQUEST",request.GET
    # for label in request.GET:
    #     try:
    #         tag=Tag.objects.get(name=label)
    #         team_list=team_list.filter(tag=tag,tag_owner__level__gte=request.GET[label])
    #     except ObjectDoesNotExist:
    #         continue
    tl = []
    for person in team_list:
        if person.first_name:
            name = person.first_name
        else:
            name = person.slack_name[:7]+"..."
        skills=[]
        for tag in person.tag_owner.all():
            skills.append(tag.tag.name)
        tl.append({
            'name': name,
            'avatar': person.slack_avatar,
            'skills': skills,
        })
    return JsonResponse(tl,safe=False)
