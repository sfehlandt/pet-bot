# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-21 03:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0006_auto_20170621_0351'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='happiness',
            field=models.IntegerField(default=0, verbose_name='Felicidaad'),
        ),
    ]
