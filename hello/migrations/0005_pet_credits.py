# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-21 03:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0004_pet_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='credits',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]