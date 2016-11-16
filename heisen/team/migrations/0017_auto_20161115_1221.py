# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-15 12:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0016_auto_20161115_0828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='progress',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='person', to='tasks.Progress'),
        ),
    ]
