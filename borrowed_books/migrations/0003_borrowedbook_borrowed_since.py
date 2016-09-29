# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-24 05:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('borrowed_books', '0002_auto_20160904_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowedbook',
            name='borrowed_since',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]