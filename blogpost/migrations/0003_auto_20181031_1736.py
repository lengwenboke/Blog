# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-10-31 09:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0002_auto_20181031_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='excerpt',
            field=models.CharField(blank=True, max_length=128, verbose_name='摘要'),
        ),
    ]