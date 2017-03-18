# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-13 01:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('researchapp', '0002_logininfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamnumber', models.CharField(max_length=15)),
                ('servicename', models.CharField(max_length=15)),
                ('ip_address', models.CharField(max_length=15)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('port', models.IntegerField()),
            ],
            options={
                'db_table': 'service',
            },
        ),
        migrations.DeleteModel(
            name='Ssh',
        ),
    ]