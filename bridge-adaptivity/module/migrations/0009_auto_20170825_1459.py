# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-25 14:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0008_merge_20170825_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='difficulty',
            field=models.CharField(choices=[(b'l', 'low'), (b'm', 'medium'), (b'h', 'high')], default=b'm', max_length=1),
        ),
    ]