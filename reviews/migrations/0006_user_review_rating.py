# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-26 02:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_auto_20160826_0239'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_review',
            name='rating',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1),
        ),
    ]
