# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-14 12:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0009_auto_20170908_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='points',
            field=models.FloatField(blank=True, default=1),
        ),
    ]