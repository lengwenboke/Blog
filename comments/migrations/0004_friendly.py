# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-11-01 01:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_auto_20181031_2158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friendly',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='网站名称')),
                ('weburl', models.URLField(max_length=128, verbose_name='网站URL')),
                ('email', models.EmailField(max_length=128, verbose_name='联系邮箱')),
                ('desc', models.TextField(verbose_name='网站说明')),
                ('reason', models.TextField(verbose_name='理由')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified_time', models.DateTimeField(blank=True, verbose_name='变更时间')),
                ('flag', models.BooleanField(default=False, verbose_name='验证')),
            ],
            options={
                'verbose_name': '友情链接',
                'verbose_name_plural': '友情链接',
                'ordering': ['-created_time'],
            },
        ),
    ]
