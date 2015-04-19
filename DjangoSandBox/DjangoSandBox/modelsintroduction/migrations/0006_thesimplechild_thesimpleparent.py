# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modelsintroduction', '0005_auto_20150327_1622'),
    ]

    operations = [
        migrations.CreateModel(
            name='TheSimpleChild',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(unique=True, max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TheSimpleParent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(unique=True, max_length=10)),
                ('child', models.ForeignKey(to='modelsintroduction.TheSimpleChild')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
