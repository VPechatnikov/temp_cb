# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('increasing', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pagestats',
            old_name='last_increase_speed',
            new_name='last_speed',
        ),
    ]
