# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2019-01-31 03:47
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0002_auto_20190130_0834'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articlepost',
            options={'ordering': ('-updated',)},
        ),
        migrations.AddField(
            model_name='articlepost',
            name='user_like',
            field=models.ManyToManyField(blank=True, related_name='articles_like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 31, 3, 47, 59, 239917, tzinfo=utc)),
        ),
    ]
