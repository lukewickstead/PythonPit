# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formsintroduction', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modelfieldstoformfields',
            name='FilePathField',
        ),
        migrations.AlterField(
            model_name='modelfieldstoformfields',
            name='ChoiceField',
            field=models.CharField(choices=[('MR', 'Mr.'), ('MRS', 'Mrs.'), ('MS', 'Ms.')], max_length=3),
        ),
    ]
