# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    sex_choices = [('MR', 'Mr.'), ('MRS', 'Mrs.'), ('MS', 'Ms.')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChildManyToMany',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('CharField', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ChildOfMany',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('CharField', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ChildOfOne',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('CharField', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ModelFieldsToFormFields',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('ChoiceField', models.CharField(choices=sex_choices, max_length=1)),
                ('CharField', models.CharField(max_length=10)),
                ('CommaSeparatedIntegerField', models.CharField(max_length=50)),
                ('EmailField', models.EmailField(max_length=254)),
                ('FilePathField', models.FilePathField()),
                ('TextField', models.TextField()),
                ('URLField', models.URLField()),
                ('DateField', models.DateField()),
                ('DateTimeField', models.DateTimeField()),
                ('TimeField', models.TimeField()),
                ('BigIntegerField', models.BigIntegerField()),
                ('BooleanField', models.BooleanField()),
                ('NullBooleanField', models.NullBooleanField()),
                ('PositiveIntegerField', models.PositiveIntegerField()),
                ('PositiveSmallIntegerField', models.PositiveSmallIntegerField()),
                ('SlugField', models.SlugField()),
                ('SmallIntegerField', models.SmallIntegerField()),
                ('DecimalField', models.DecimalField(decimal_places=2, max_digits=5)),
                ('FloatField', models.FloatField()),
                ('IntegerField', models.IntegerField()),
                ('GenericIPAddressField', models.GenericIPAddressField()),
                ('ForeignKey', models.ForeignKey(to='formsintroduction.ChildOfMany')),
                ('ManyToManyField', models.ManyToManyField(to='formsintroduction.ChildManyToMany')),
                ('OneToOneField', models.OneToOneField(to='formsintroduction.ChildOfOne')),
            ],
        ),
    ]
