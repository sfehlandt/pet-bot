# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-21 05:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pet_bot', '0004_taks'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Taks',
            new_name='Task',
        ),
    ]