# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('increasing', '0002_auto_20150211_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagestats',
            name='cur_avg',
            field=models.FloatField(null=True),
        ),
    ]
