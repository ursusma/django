# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-22 13:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('huiuapp', '0002_auto_20160901_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rank',
            name='createdTime',
            field=models.IntegerField(),
        ),
    ]
