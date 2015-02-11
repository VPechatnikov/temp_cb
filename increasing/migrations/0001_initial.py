# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PageStats',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('host', models.CharField(max_length=120)),
                ('page_title', models.TextField(null=True, blank=True)),
                ('page_path', models.CharField(max_length=500)),
                ('cur_avg', models.FloatField()),
                ('new_avg', models.FloatField()),
                ('num_new_points', models.IntegerField(default=0)),
                ('increasing', models.BooleanField(default=False)),
                ('last_increase_speed', models.FloatField()),
                ('updated', models.DateTimeField(auto_now=True, auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='pagestats',
            unique_together=set([('host', 'page_path')]),
        ),
        migrations.AlterIndexTogether(
            name='pagestats',
            index_together=set([('host', 'page_path')]),
        ),
    ]
