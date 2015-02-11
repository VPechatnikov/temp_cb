# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('increasing', '0003_auto_20150211_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagestats',
            name='new_avg',
            field=models.FloatField(null=True),
        ),
    ]
