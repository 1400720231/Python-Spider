# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-02-20 18:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20180220_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='url',
            field=models.CharField(default='', max_length=200, verbose_name='访问地址'),
        ),
    ]
