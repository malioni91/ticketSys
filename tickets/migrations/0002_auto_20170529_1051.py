# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 10:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='completed',
            new_name='status',
        ),
    ]
