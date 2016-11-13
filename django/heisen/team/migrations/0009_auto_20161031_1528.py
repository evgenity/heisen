# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-31 15:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0008_person_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(default=0)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tag_owner', to='team.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('child_tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.Tag')),
                ('persons', models.ManyToManyField(through='team.Level', to='team.Person')),
            ],
        ),
        migrations.AddField(
            model_name='level',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tag_name', to='team.Tag'),
        ),
    ]
