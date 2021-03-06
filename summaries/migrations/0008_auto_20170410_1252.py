# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-04-10 15:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('summaries', '0007_summaryanswer_non_functional_ratings'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodeSmellOpinion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opinion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SummaryType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='summaryanswercodesmell',
            name='is_smell',
        ),
        migrations.AddField(
            model_name='summaryanswercodesmell',
            name='was_important',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='summaryanswercodesmell',
            name='opinion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='summaries.CodeSmellOpinion'),
        ),
    ]
