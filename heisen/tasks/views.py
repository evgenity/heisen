# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.core.exceptions import ObjectDoesNotExist

from team.models import Person
from tasks.models import Task, Reaction
from home.models import Channel


class IndexView(generic.ListView):
    template_name = 'tasks/index.html'
    context_object_name = 'tasks_list'
    def get_queryset(self):
        return Task.objects.all().order_by('-number')

def progress(request):
    template_name = 'tasks/progress.html'
    th=[]
    th.extend(['T'+str(i)for i in range (Task.objects.count())])
    print th
    return render(request, template_name,context={'progress':progress,'th':th})


def update(request):
    import requests
    import json
    import re
    import Slackbot as sb
    # print(json.dumps(sb.filter_messages(sb.get_channel_history(sb.tasks_channel),'^([TТ])\d+'),
    #                       sort_keys=True,indent=4, separators=(',', ': ')))
    for task in sb.filter_messages(sb.get_channel_history(sb.tasks_channel), '^([ТT])\d+'):
        try:
            task_model = Task.objects.get(number = int(task[0][1:]))
        except ObjectDoesNotExist:
            task_model = Task(number = int(task[0][1:]))
        task_model.task_text = re.sub('^([ТT])\d+[\.\s-]+',"",sb.htmlize_links(task[1]['text']))
        task_model.save()
        try:
            for reaction in task[1]['reactions']:
                for user in reaction['users']:
                    reaction_model = Reaction(
                        task_id = task_model,
                        user_id = Person.objects.get(slack_id=user),
                        emoji_text = reaction['name']
                    )
                    reaction_model.save()
        except KeyError:
            pass
    for channel in sb.get_channels():
        try:
            channel_model = Channel.objects.get(channel_id=channel['id'])
            channel_model.name = channel['name']
        except ObjectDoesNotExist:
            channel_model = Channel(channel_id=channel['id'],name=channel['name'])
        channel_model.save()
    print
    return redirect('/tasks')
