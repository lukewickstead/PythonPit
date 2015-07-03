# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneAddress',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('number', models.IntegerField()),
                ('street_name', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PhoneContact',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(unique=True, max_length=20)),
                ('surname', models.CharField(unique=True, max_length=20)),
                ('height', models.FloatField()),
                ('date_of_birth', models.DateField()),
                ('is_family', models.BooleanField(default=False)),
                ('sex', models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE')], max_length=1)),
                ('address', models.OneToOneField(to='viewsintroduction.PhoneAddress')),
            ],
        ),
    ]
