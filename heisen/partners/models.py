from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

# Create your models here
@python_2_unicode_compatible
class Partner(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=800)
    image = models.CharField(max_length=500)
    url = models.CharField(max_length=100, default="")
    #image = models.ImageField() ????
    def __str__(self):
        #return "{}. {}".format(self.name,self.description)
        return self.name
