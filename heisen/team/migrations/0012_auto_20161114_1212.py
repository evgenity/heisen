# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-14 12:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0011_person_thanked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='level',
            name='person',
        ),
        migrations.RemoveField(
            model_name='level',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='child_tag',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='persons',
        ),
        migrations.DeleteModel(
            name='Level',
        ),
    ]
