# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-03 16:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20180303_2323'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bloggerprofile',
            old_name='blogger',
            new_name='user',
        ),
    ]
