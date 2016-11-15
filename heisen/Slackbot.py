#!venv/bin/Python3
# -*- coding: utf-8 -*-
import json
import re
import collections
import os.path
import time

import requests
import emoji

from home.models import Channel
from team.models import Person
Slacktoken = os.environ['SLACK_TOKEN']

'''emoji_list={
    "+1":"👍",
    "the_horns":"🤘",
    "sweat_smile":"😅",
    "rage":"😡",
    "ZZZ":"💤",}'''
#https://api.slack.com - Slack API
#https://api.slack.com/docs/oauth  - to get token
tasks_channel='C2A76BCRZ'
project_channel='C2A5C1JBY'

def get_channels():
    url="https://slack.com/api/channels.list?token="+Slacktoken
    r=requests.get(url)
    channels=json.loads(r.text)
    return channels['channels']

def get_channel_messages(channel_id,latest='now'):
    if (latest=="now"):
        url="https://slack.com/api/channels.history?token="+Slacktoken+"&channel="+channel_id+"&unreads=1&pretty=1"
    else:
        url="https://slack.com/api/channels.history?token="+Slacktoken+"&channel="+channel_id+"&unreads=1&pretty=1&latest="+latest

    r=requests.get(url)
    messages_body=json.loads(r.text)
    try:
        return messages_body["messages"], messages_body["has_more"], messages_body["messages"][-1]["ts"]
    except IndexError:
        return messages_body["messages"], messages_body["has_more"], 0

def get_channel_history(channel_id):
    messages, has_more, latest =get_channel_messages(channel_id)
    while(has_more):
        new_messages, has_more, latest =get_channel_messages(channel_id,latest=latest)
        messages.extend(new_messages)
        get_channel_messages(channel_id,latest)
    return messages

def filter_messages(messages,regexp):
    for message in messages:
        if message['text'][0].encode('utf-8')=="Т":
            message['text'] = "T"+message['text'][1:] #I gave up
    return [ (re.search(regexp, message['text']).group(0),message)  for message in messages if message['type']=="message" and re.match(regexp,message['text'])]

def linkrepl( match ):
    split = match.group()[1:-1].split(r'|')
    address = split[0]
    if address[0] == "#":
        address = "https://heisenspaces.slack.com/messages/"+Channel.objects.get(channel_id=address[1:]).name
    elif address[0] == "@":
        name= Person.objects.get(slack_id=address[1:]).slack_name
        address = "https://heisenspaces.slack.com/team/" + name
        text = name
        return "<a href='{address}'>{text}</a>".format(address=address,text=text)
    if len(split)==2:
        text = split[1]
        return "<a href='{address}'>{text}</a>".format(address=address,text=text)
    else:
        return "<a href='{address}'>{text}</a>".format(address=address,text=address)

def htmlize_links(string):
    p = re.compile('\<(.*?)(\|.*?)?\>')
    return p.sub(linkrepl, string)


def get_persons(messages):
    persons=[]
    for message in messages:
        if message['type']=="message" \
                        and re.search('\<(.*?)(\|.*?)?\>',message['text']) \
                        and re.search('\<(.*?)(\|.*?)?\>',message['text']).group(1)[0]=="@":
            if "subtype" not in message.keys():
                persons.append(re.search('\<(.*?)(\|.*?)?\>',message['text']).group(1)[1:])
    return persons
