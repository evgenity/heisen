# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-19 16:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='first_name',
            field=models.CharField(default='1', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='last_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='slack_id',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='avatar',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='person',
            name='displayed_name',
            field=models.CharField(max_length=50),
        ),
    ]
