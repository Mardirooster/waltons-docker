# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0003_auto_20160815_1747'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
