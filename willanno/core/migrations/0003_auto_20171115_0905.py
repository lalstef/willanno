# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 09:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20171115_0905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inkdocument',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='inkdocumentannotation',
            name='created_by',
        ),
    ]
