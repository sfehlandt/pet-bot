# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-22 05:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet_bot', '0009_auto_20170621_0148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='status',
        ),
        migrations.AddField(
            model_name='pet',
            name='state',
            field=models.IntegerField(choices=[(0, 'ok'), (1, 'aburrido'), (2, 'hambriento'), (3, 'con frío'), (4, 'sucio'), (5, 'enfermo'), (6, 'herido'), (7, 'triste')], default=0, verbose_name='estado'),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.IntegerField(choices=[(0, 'Terminada'), (1, 'Pendiente'), (2, 'En progreso')], default=1, verbose_name='estado'),
        ),
    ]
