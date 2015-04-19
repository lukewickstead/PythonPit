# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modelsintroduction', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TheSimpleModel',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('string_field', models.CharField(max_length=20)),
                ('decimal_field', models.IntegerField()),
                ('dateTime_field', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='address',
            name='person',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
