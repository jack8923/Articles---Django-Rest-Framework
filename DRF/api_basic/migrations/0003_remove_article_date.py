# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-28 13:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0002_auto_20200428_1316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='date',
        ),
    ]
