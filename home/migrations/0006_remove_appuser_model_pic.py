# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-11 17:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20171211_1700'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appuser',
            name='model_pic',
        ),
    ]