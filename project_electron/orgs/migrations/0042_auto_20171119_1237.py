# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-19 17:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orgs', '0041_auto_20171119_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='baginfometadata',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orgs.LanguageCode'),
        ),
        migrations.AddField(
            model_name='baginfometadata',
            name='record_creators',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orgs.RecordCreators'),
        ),
        migrations.AddField(
            model_name='baginfometadata',
            name='source_organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orgs.Organization'),
        )
    ]
