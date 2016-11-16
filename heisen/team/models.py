from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
import datetime
from django.db import models
from django.contrib.auth.models import User
#from tasks.models import Progress


@python_2_unicode_compatible
class Person(models.Model):
    full_name = models.CharField(max_length=200,blank=True)
    first_name = models.CharField(max_length=100,blank=True)
    last_name = models.CharField(max_length=100,blank=True)
    displayed_name = models.CharField(max_length=50,blank=True)
    slack_id = models.CharField(max_length=20)
    slack_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50,blank=True)
    cv_link = models.CharField(max_length=200,blank=True)
    email = models.CharField(max_length=200,blank=True)
    avatar = models.CharField(max_length=400) #image link
    slack_avatar = models.CharField(max_length=400, default='')
    thanked = models.BooleanField(default=False)
    thanks = models.ManyToManyField('self', through='Thank', symmetrical=False)
    rating = models.IntegerField(default=0)
    progress = models.OneToOneField('tasks.Progress', null=True, blank=True, related_name="person")
    user = models.OneToOneField(User,related_name = 'person',default=None,null=True, blank=True)
    def __str__(self):
        if self.full_name:
            return self.full_name
        else:
            return self.slack_name

@python_2_unicode_compatible
class Thank(models.Model):
    giver = models.ForeignKey(Person,related_name = 'giver', on_delete=models.CASCADE)
    receiver = models.ForeignKey(Person, related_name = 'receiver', on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    def __str__(self):
        #return "{} thanked {} with text: {}".format(self.giver,self.receiver,self.text)
        return self.giver.full_name+" thanked "+self.receiver.full_name+" with text: "+self.text

@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    persons = models.ManyToManyField(Person,related_name="tags")
    def __str__(self):
        return self.name
