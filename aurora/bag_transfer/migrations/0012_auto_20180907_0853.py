# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-07 12:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bag_transfer', '0011_auto_20180731_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accession',
            name='accession_number',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
