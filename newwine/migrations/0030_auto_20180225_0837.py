# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-02-25 08:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newwine', '0029_auto_20180225_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='image',
            field=models.FileField(upload_to='carousel/', verbose_name='File'),
        ),
    ]
