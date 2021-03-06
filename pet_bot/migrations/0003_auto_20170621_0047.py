# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-21 04:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet_bot', '0002_auto_20170621_0027'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='species',
            field=models.CharField(default='Cat', max_length=30, verbose_name='especie'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pet',
            name='credits',
            field=models.IntegerField(default=0, verbose_name='créditos'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='happiness',
            field=models.IntegerField(default=0, verbose_name='felicidaad'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='name',
            field=models.CharField(max_length=30, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='owner',
            field=models.CharField(max_length=15, verbose_name='dueño'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='status',
            field=models.IntegerField(default=0, verbose_name='estado'),
        ),
    ]
