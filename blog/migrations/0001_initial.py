# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-11 05:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=63)),
                ('slug', models.SlugField()),
                ('text', models.TextField()),
                ('pub_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Startup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=31)),
                ('slug', models.SlugField()),
                ('description', models.TextField()),
                ('founded_date', models.DateField()),
                ('contact', models.EmailField(max_length=254)),
                ('website', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='startups',
            field=models.ManyToManyField(to='blog.Startup'),
        ),
    ]
