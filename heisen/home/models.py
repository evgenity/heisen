from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
import datetime
from django.db import models

# Create your models here.
@python_2_unicode_compatible
class Channel(models.Model):
    channel_id = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
