# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-20 11:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0004_auto_20161020_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]