# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-29 06:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='datetables',
            fields=[
                ('dateID', models.AutoField(primary_key=True, serialize=False)),
                ('dateName', models.CharField(max_length=64)),
                ('createdTime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
