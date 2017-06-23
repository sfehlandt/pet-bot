# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-21 05:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pet_bot', '0006_auto_20170621_0115'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='pet',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='pet_bot.Pet', verbose_name='mascota'),
            preserve_default=False,
        ),
    ]