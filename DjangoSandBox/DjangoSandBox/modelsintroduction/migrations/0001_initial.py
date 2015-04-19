# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('line_one', models.CharField(max_length=30)),
                ('line_two', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('county', models.CharField(max_length=30)),
                ('post_code', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=3, choices=[('Mr', 'Mr'), ('Mrs', 'Mrs')])),
                ('first_name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=30)),
                ('height', models.DecimalField(max_digits=6, decimal_places=2)),
                ('date_of_birth', models.DateTimeField()),
                ('telephone_number', models.CharField(max_length=20)),
                ('email_address', models.EmailField(max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='address',
            name='person',
            field=models.ManyToManyField(to='modelsintroduction.Person'),
            preserve_default=True,
        ),
    ]
