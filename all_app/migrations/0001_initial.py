# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-02 17:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(default=datetime.datetime(2017, 9, 2, 17, 31, 31, 454461))),
                ('FbToken', models.CharField(max_length=200)),
                ('TwToken', models.CharField(max_length=200)),
                ('InToken', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
