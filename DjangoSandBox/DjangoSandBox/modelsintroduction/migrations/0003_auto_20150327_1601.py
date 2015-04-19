# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modelsintroduction', '0002_auto_20150327_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thesimplemodel',
            name='string_field',
            field=models.CharField(max_length=20, unique=True),
            preserve_default=True,
        ),
    ]
