# -*- coding: utf-8 -*-
import os
import requests
import json
import re
import Slackbot as sb
from django.core.exceptions import ObjectDoesNotExist

from team.models import Person, Tag
from tasks.models import Task, Reaction, Progress
from home.models import Channel

def update_avatar(icon,link,user):
    if re.match("^https:\/\/avatars\.slack-edge\.com",link):
        user.avatar=1
    else:
        gurl=link.split("?")[0]+"?d=blank&s=1"
        r=requests.get(gurl)
        if icon == r.content:
            user.avatar=0
        else:
            user.avatar=1


def update_team(break_user=None):
    Slacktoken=os.environ['SLACK_TOKEN']
    url="https://slack.com/api/users.list?token="+Slacktoken
    r=requests.get(url)
    users=json.loads(r.text)
    f1=open(os.path.dirname(os.path.realpath(__file__))+"/templates/static/images/gravico.png","r")
    gravico=f1.read()
    for user in users['members']:
        if break_user and user['name']!=break_user:
            continue
        try: email = user['profile']['email']
        except KeyError: continue
        try:
            user_model = Person.objects.get(slack_id=user['id'])
        except ObjectDoesNotExist:
            user_model = Person()
            progress = Progress()
            progress.save()
            user_model.progress = progress
        #AVATAR PART
        update_avatar(icon=gravico,link=user['profile']['image_192'],user=user_model)
        try: user_model.full_name = user['profile']['real_name']
        except KeyError: user_model.full_name = user['name']
        try: user_model.first_name = user['profile']['first_name']
        except KeyError: user_model.first_name = ""
        try: user_model.last_name = user['profile']['last_name']
        except KeyError: last_name=""
        user_model.slack_name = user['name']
        user_model.slack_id=user['id']
        user_model.slack_avatar=user['profile']['image_192']
        user_model.email = user['profile']['email']
        user_model.save()
        if break_user:
            return user_model

def update_channels():
    for channel in sb.get_channels():
        try:
            channel_model = Channel.objects.get(channel_id=channel['id'])
            channel_model.name = channel['name']
        except ObjectDoesNotExist:
            channel_model = Channel(channel_id=channel['id'],name=channel['name'])
        channel_model.save()

def update_tasks():
    Reaction.objects.all().delete()
    for task in sb.filter_messages(sb.get_channel_history(sb.tasks_channel), '^([TТ])\d+'):
        try:
            task_model = Task.objects.get(number = int(task[0][1:]))
        except ObjectDoesNotExist:
            task_model = Task(number = int(task[0][1:]))
        task_model.task_text = re.sub('^([ТT])\d+[\.\s-]+',"",sb.htmlize_links(task[1]['text']))
        task_model.save()
        try:
            for reaction in task[1]['reactions']:
                for user in reaction['users']:
                    try:
                        reaction_model = Reaction.objects.get(task_id = task_model,user_id = Person.objects.get(slack_id=user))
                    except ObjectDoesNotExist:
                        reaction_model = Reaction(
                            task_id = task_model,
                            user_id = Person.objects.get(slack_id=user),
                        )
                    reaction_model.emoji_text = reaction['name']
                    reaction_model.task_number = int(task[0][1:])
                    reaction_model.save()
        except KeyError:
            pass
    for person in Person.objects.all():
        person.progress.update_rating()

def update_thanks():
    channel=Channel.objects.get(name="manythanks").channel_id
    persons=sb.get_persons(sb.get_channel_history(channel))
    for slack_id in persons:
        person_model=Person.objects.get(slack_id=slack_id)
        person_model.thanked=True
        person_model.save()

def update_tags():
    channel=Channel.objects.get(name="hashtags").channel_id
    for tag in sb.filter_messages(sb.get_channel_history(channel), '^([A-Za-z0-9:_])+'):
        tag_model = Tag.objects.get_or_create(name=tag[0])[0]
        tag_model.description = tag[1]['text']
        try:
            for reaction in tag[1]['reactions']:
                for user in reaction['users']:
                    user_model = Person.objects.get(slack_id=user)
                    user_model.tags.add(tag_model)
                    user_model.save()
        except KeyError:
            pass
        tag_model.save()




def updater():
    update_channels()
    update_team()
    update_tasks()
    update_tags()
    update_thanks()
