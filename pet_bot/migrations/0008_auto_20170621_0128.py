# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-21 05:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pet_bot', '0007_task_pet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='pet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='pet_bot.Pet', verbose_name='mascota'),
        ),
    ]
