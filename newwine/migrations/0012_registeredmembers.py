# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-07 17:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newwine', '0011_photoalbum_caption'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisteredMembers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('other_names', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(max_length=6)),
                ('date_of_birth', models.DateField()),
                ('course', models.CharField(max_length=150)),
                ('year', models.CharField(max_length=10)),
                ('hall_or_hostel', models.CharField(max_length=100)),
                ('room', models.CharField(max_length=10)),
                ('department', models.CharField(max_length=70)),
                ('covenant_family', models.CharField(max_length=100)),
                ('home_temple', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=14)),
            ],
        ),
    ]
