# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modelsadvanced', '0002_auto_20150629_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='parent',
            field=models.ForeignKey(null=True, to='modelsadvanced.Parent'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='name',
            field=models.CharField(null=True, max_length=10, unique=True),
        ),
    ]
