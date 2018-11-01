# Generated by Django 2.1.2 on 2018-11-01 15:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0009_broadcast_is_activate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='broadcast',
            name='post',
            field=models.ForeignKey(on_delete=True, to='blogpost.Post', verbose_name='文章详情'),
        ),
        migrations.AlterField(
            model_name='category',
            name='navigation',
            field=models.ForeignKey(on_delete=True, to='blogpost.Navigation'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=True, to=settings.AUTH_USER_MODEL, verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(on_delete=True, to='blogpost.Category', verbose_name='分类'),
        ),
    ]
