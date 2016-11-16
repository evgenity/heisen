from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
import datetime
from django.db import models
from heisen.team.models import Person

# Create your models here


@python_2_unicode_compatible
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=600)
    source_code = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    project_manager = models.ForeignKey(Person, on_delete=models.CASCADE)
    def __str__(self):
        return "Project: {1}".format(self.name)

@python_2_unicode_compatible
class Role(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)
    role_description = models.CharField(max_length=200)

@python_2_unicode_compatible
class Project_reaction(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    emoji_text = models.CharField(max_length=20)
    user_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    def __str__(self):
        return "{1} reacted for project {2}: {3}".format(self.user_id,self.task_id,self.emoji_text) #ALARM
