# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-16 06:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import user_profile.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ReunionSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('picture', models.ImageField(default='reunion_site_directory/no-image.jpg', upload_to=user_profile.models.reunionSite_directory_path)),
                ('address', models.TextField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_profile.Area')),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('picture', models.ImageField(default='university_directory/no-img.jpg', upload_to=user_profile.models.university_directory_path)),
                ('reunion_sites', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_profile.ReunionSite')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=500, null=True)),
                ('studentID', models.CharField(max_length=10)),
                ('picture', models.ImageField(default='pic_folder/None/no-img.jpg', upload_to=user_profile.models.user_directory_path)),
                ('video', models.URLField(blank=True, null=True)),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_profile.Career')),
                ('subjects', models.ManyToManyField(to='user_profile.Subject')),
                ('university', models.ManyToManyField(to='user_profile.University')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
