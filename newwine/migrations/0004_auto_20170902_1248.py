# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-02 12:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('newwine', '0003_quote_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='carousel',
            name='added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mainevent',
            name='added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
