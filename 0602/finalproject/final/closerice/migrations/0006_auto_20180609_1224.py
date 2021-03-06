# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-09 04:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('closerice', '0005_auto_20180608_2219'),
    ]

    operations = [
        migrations.CreateModel(
            name='restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('content', models.TextField(blank=True)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('price', models.CharField(blank=True, max_length=100)),
                ('worktime', models.CharField(blank=True, max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='imageforrestaurant')),
            ],
        ),
        migrations.DeleteModel(
            name='Restaurants',
        ),
    ]
