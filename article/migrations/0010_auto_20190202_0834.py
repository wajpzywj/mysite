# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2019-02-02 08:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0009_auto_20190202_0329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 2, 8, 34, 39, 444960, tzinfo=utc)),
        ),
    ]