# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-21 19:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('all_app', '0007_auto_20170921_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 21, 21, 30, 48, 732237)),
        ),
    ]