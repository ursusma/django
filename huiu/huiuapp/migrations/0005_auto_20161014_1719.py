# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-14 09:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('huiuapp', '0004_rank_rankweb'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('systime', models.TextField()),
                ('usersnumber', models.TextField()),
                ('loadavg', models.TextField()),
                ('cpufree', models.TextField()),
                ('momeryfree', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='rank',
            name='RankID',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='rank',
            name='createdTime',
            field=models.TextField(),
        ),
    ]