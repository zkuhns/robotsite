# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-23 23:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_auto_20170423_2320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='hide_email',
        ),
        migrations.RemoveField(
            model_name='member',
            name='hide_phone',
        ),
        migrations.AddField(
            model_name='member',
            name='email_accessibility',
            field=models.BooleanField(choices=[(False, 'PRIVATE'), (True, 'PUBLIC')], default=True, verbose_name='Email Accessibility'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='phone_accessibility',
            field=models.BooleanField(choices=[(False, 'PRIVATE'), (True, 'PUBLIC')], default=True, verbose_name='Phone Accessibility'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='member',
            name='member_accessibility',
            field=models.BooleanField(choices=[(False, 'PRIVATE'), (True, 'PUBLIC')], verbose_name='Member Accessibility'),
        ),
    ]
