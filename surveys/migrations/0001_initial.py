# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-04-05 17:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubjectCharacterizationSurvey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('education', models.CharField(choices=[('Doutorado', 'Doutorado'), ('Mestrado', 'Mestrado'), ('Gradua\xe7\xe3o', 'Gradua\xe7\xe3o'), ('Curso T\xe9cnico', 'Curso T\xe9cnico'), ('Sem Educa\xe7\xe3o Formal', 'N\xe3o possuo educa\xe7\xe3o formal em computa\xe7\xe3o')], default='Sem Educa\xe7\xe3o Formal', max_length=30, verbose_name='Selecione sua maior titula\xe7\xe3o na \xe1rea de computa\xe7\xe3o ou \xe1rea afins')),
                ('experience', models.IntegerField(max_length=2, verbose_name='Experi\xeancia em desenvolvimento de software (em anos) na ind\xfastria')),
                ('experience_java', models.IntegerField(max_length=2, verbose_name='Experi\xeancia com linguagem de programa\xe7\xe3o Java (em anos) na ind\xfastria')),
                ('projects_java', models.IntegerField(max_length=2, verbose_name='Quantos projetos em Java voc\xea trabalhou na ind\xfastria?')),
            ],
        ),
    ]