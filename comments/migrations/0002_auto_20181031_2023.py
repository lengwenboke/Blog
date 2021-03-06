# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-10-31 12:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_time'], 'verbose_name': '评论', 'verbose_name_plural': '评论'},
        ),
        migrations.AddField(
            model_name='comment',
            name='author_reply',
            field=models.TextField(blank=True, verbose_name='作者回复'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogpost.Post', verbose_name='文章'),
        ),
    ]
