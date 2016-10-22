from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.core.exceptions import ObjectDoesNotExist

from team.models import Person

class IndexView(generic.ListView):
    template_name = 'team/index.html'
    context_object_name = 'team_list'
    def get_queryset(self):
        return Person.objects.exclude(avatar="",slack_avatar="").exclude(full_name="").order_by('-rating','full_name')

def update(request):
    import requests
    import json
    import os
    Slacktoken=os.environ['SLACK_TOKEN']
    url="https://slack.com/api/users.list?token="+Slacktoken
    r=requests.get(url)
    users=json.loads(r.text)
    for user in users['members']:
            try:
                import re
                user_model = Person.objects.get(slack_id=user['id'])
                if not re.match('https:\/\/avatars.slack-edge.com',user['profile']['image_192']):
                    user_model.slack_avatar = user['profile']['image_192']
                else:
                    user_model.slack_avatar = ""

                user_model.save()
            except ObjectDoesNotExist:
                try: full_name = user['profile']['real_name']
                except KeyError: full_name = user['name']
                try: first_name = user['profile']['first_name']
                except KeyError: first_name = ""
                try: last_name = user['profile']['last_name']
                except KeyError: last_name=""
                try: email = user['profile']['email']
                except KeyError: email=""
                if email:
                    user_model=Person(
                        full_name = full_name ,
                        first_name = first_name ,
                        last_name = last_name,
                        slack_id = user['id'],
                        slack_name = user['name'],
                        email = user['profile']['email'],
                        slack_avatar = user['profile']['image_192']
                    )
                    user_model.save()
    return redirect('/team')
