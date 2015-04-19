# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modelsintroduction', '0004_auto_20150327_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thesimplemodel',
            name='dateTime_field',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='thesimplemodel',
            name='integer_field',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
