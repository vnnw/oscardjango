# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-24 16:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraddress',
            name='customer_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Deliver to name'),
        ),
        migrations.AddField(
            model_name='useraddress',
            name='detail_address',
            field=models.CharField(blank=True, help_text='It is advisable to fill in the detailed receipt address, such as street name, house number, floor and room number', max_length=255, verbose_name='Shipping address:'),
        ),
    ]