# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-23 20:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('contact_email', models.CharField(max_length=255)),
                ('contact_phone', models.CharField(max_length=255)),
                ('join_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
