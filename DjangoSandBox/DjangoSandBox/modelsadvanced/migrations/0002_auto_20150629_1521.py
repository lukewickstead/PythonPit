# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modelsadvanced', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='parent',
            field=models.ForeignKey(blank=True, to='modelsadvanced.Parent'),
        ),
    ]
