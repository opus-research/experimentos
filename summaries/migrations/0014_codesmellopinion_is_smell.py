# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-04-11 03:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summaries', '0013_designproblem'),
    ]

    operations = [
        migrations.AddField(
            model_name='codesmellopinion',
            name='is_smell',
            field=models.BooleanField(default=False),
        ),
    ]
