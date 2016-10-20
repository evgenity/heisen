from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
import datetime
from django.db import models
from team.models import Person


# Create your models here


@python_2_unicode_compatible
class Task(models.Model):
    number = models.IntegerField()
    task_text = models.CharField(max_length=1500)
    reactions = models.ManyToManyField(Person, through='Reaction')
    def __str__(self):
        #return "T{number}. {text}".format(number=self.number,text=self.task_text)
        return "T"+str(self.number)




@python_2_unicode_compatible
class Reaction(models.Model):
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    emoji_text = models.CharField(max_length=20)
    user_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    def __str__(self):
        return "{1} reacted for task {2}: {3}".format(self.user_id,self.task_id,self.emoji_text) #ALARM
