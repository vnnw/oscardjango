# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-25 01:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0002_auto_20170524_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='customer_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Name'),
        ),
    ]