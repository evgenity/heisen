# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-14 13:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0013_tag_persons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='user',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='person', to=settings.AUTH_USER_MODEL),
        ),
    ]
