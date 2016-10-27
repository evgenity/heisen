from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.admin.views.decorators import staff_member_required

from team.models import Person
from tasks.models import Progress

class IndexView(generic.ListView):
    template_name = 'team/index.html'
    context_object_name = 'team_list'
    def get_queryset(self):
        return Person.objects.exclude(avatar="",slack_avatar="").order_by('-progress__rating')
