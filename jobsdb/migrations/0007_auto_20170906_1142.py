# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-06 08:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobsdb', '0006_auto_20170906_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='location_name',
            field=models.CharField(max_length=10),
        ),
    ]
