# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-28 02:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickfireQuestions', '0006_question_isanswered'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='isCorrectAnswer',
            field=models.BooleanField(default=False),
        ),
    ]
