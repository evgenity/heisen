# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.admin.views.decorators import staff_member_required

from team.models import Person
from tasks.models import Task, Reaction, Progress
from home.models import Channel


class IndexView(generic.ListView):
    template_name = 'tasks/index.html'
    context_object_name = 'tasks_list'
    def get_queryset(self):
        return Task.objects.all().order_by('-number')

def progress(request):
    if request.user.is_authenticated():
        import emoji
        template_name = 'tasks/progress.html'
        th=[]
        th.extend([['T'+str(i+1),Task.objects.get(number=i+1).task_text]for i in range (Task.objects.count())])
        tb=[]
        for person in Person.objects.all().order_by('-progress__task_progress'):
            tb.append([person.slack_name.encode('utf-8'),["" for i in range(Task.objects.count())]])
            #tb.append([person.slack_name].extend(["" for i in range (Task.objects.count())]))
        for reaction in Reaction.objects.all():
            if reaction.emoji_text == "the_horns":
                emoji_text = "🤘"
            else:
                emoji_text = emoji.emojize(":"+reaction.emoji_text.encode('utf-8')+":", use_aliases=True)
            for t in tb:
                if t[0]==reaction.user_id.slack_name:
                    t[1][reaction.task_number - 1] = emoji_text
        return render(request, template_name,context={'progress':tb,'th':th})
    else:
        return render(request, "tasks/login_failed.html")
