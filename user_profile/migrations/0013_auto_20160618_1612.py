# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-18 20:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0012_auto_20160617_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user_profile.Area'),
        ),
    ]
