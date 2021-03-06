# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-01 08:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(choices=[('SG', 'Singapore')], default='SG', max_length=4)),
                ('gender', models.CharField(choices=[('M', 'Female'), ('F', 'Male')], default='F', max_length=2)),
                ('zip_code', models.CharField(max_length=10)),
                ('birthday', models.DateTimeField(null=True)),
                ('home_address', models.TextField()),
                ('mobile_no', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
