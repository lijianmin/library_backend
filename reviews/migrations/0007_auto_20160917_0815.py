# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-17 08:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_user_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_review',
            name='reviewed_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='user_review',
            name='reviewed_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
