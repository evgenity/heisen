# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-15 07:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0014_auto_20161114_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='progress',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.Progress'),
        ),
    ]
