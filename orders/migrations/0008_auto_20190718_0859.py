# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2019-07-18 08:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20190718_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.DecimalField(decimal_places=5, default='', max_digits=50),
        ),
    ]
