# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-12-03 01:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hello', '0022_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='cooperative',
        ),
        migrations.AddField(
            model_name='producer',
            name='is_producer',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='producer',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
