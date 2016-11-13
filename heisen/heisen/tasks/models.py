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
    task_number = models.IntegerField()
    emoji_text = models.CharField(max_length=20)
    user_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.user_id)

@python_2_unicode_compatible
class Progress(models.Model):
    hidden_rating = models.IntegerField(default=0)
    task_progress = models.IntegerField(default=0)
    project_value = models.IntegerField(default=0)
    photo_penalty = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    def tasks_count(self):
        return Reaction.objects.filter(user_id=self.person).count()
    def update_rating(self):
        self.task_progress = 0
        for reaction in Reaction.objects.filter(user_id=self.person):
            if reaction.emoji_text == "":
                self.task_progress += 0
            elif reaction.emoji_text == "rage":
                self.task_progress += 2
            elif reaction.emoji_text == "sweat_smile":
                self.task_progress += 5
            elif reaction.emoji_text == "clap":
                self.task_progress += 7
            elif reaction.emoji_text == "+1":
                self.task_progress += 8
            elif reaction.emoji_text == "the_horns":
                self.task_progress += 10
            elif reaction.emoji_text == "fire":
                self.task_progress += 10
        self.rating = self.hidden_rating + self.task_progress + self.project_value + self.photo_penalty
        self.save()
        return self.rating




    def __str__(self):
        #return "T{number}. {text}".format(number=self.number,text=self.task_text)
        return "Progress of "+str(self.person.slack_name)
