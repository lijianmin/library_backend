# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-25 15:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20160822_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='borrowed',
            field=models.BooleanField(default=False),
        ),
    ]
