# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import modelsadvanced.models
import django.core.validators


class Migration(migrations.Migration):
    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractBaseChild',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(unique=True, max_length=10)),
                ('age', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(unique=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(unique=True, max_length=10)),
                ('authors', models.ManyToManyField(to='modelsadvanced.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(unique=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ContactDetails',
            fields=[
                ('id', models.AutoField(primary_key=True,
                                        auto_created=True,
                                        verbose_name='ID',
                                        serialize=False)),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(10),
                                                        django.core.validators.MaxValueValidator(100)])),
                ('name', models.CharField(validators=[django.core.validators.MinLengthValidator(10),
                                                      django.core.validators.MaxLengthValidator(10),
                                                      django.core.validators.RegexValidator('^[A-Z][a-z]{1,}$')],
                                          max_length=20)),
                ('contactDate', models.DateField(validators=[modelsadvanced.models.is_future_date_validator])),
            ],
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Man',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='MultiTableBaseParent',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(unique=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(null=True, blank=True, unique=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ProxyParent',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(unique=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='MultiTableBaseChild',
            fields=[
                ('multitablebaseparent_ptr',
                 models.OneToOneField(primary_key=True,
                                      to='modelsadvanced.MultiTableBaseParent', parent_link=True,
                                      auto_created=True, serialize=False)),
                ('age', models.IntegerField()),
            ],
            bases=('modelsadvanced.multitablebaseparent',),
        ),
        migrations.AddField(
            model_name='dog',
            name='owner',
            field=models.OneToOneField(blank=True, to='modelsadvanced.Man', null=True),
        ),
        migrations.AddField(
            model_name='child',
            name='parent',
            field=models.ForeignKey(to='modelsadvanced.Parent'),
        ),
        migrations.CreateModel(
            name='ProxyChild',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('modelsadvanced.proxyparent',),
        ),
    ]
