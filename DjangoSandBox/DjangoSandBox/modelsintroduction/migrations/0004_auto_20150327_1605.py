# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modelsintroduction', '0003_auto_20150327_1601'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thesimplemodel',
            old_name='decimal_field',
            new_name='integer_field',
        ),
    ]
