# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-08 02:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Things',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('status', models.TextField(default=0)),
            ],
        ),
    ]
