# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0005_auto_20160815_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='lessonname',
            field=models.CharField(default='NA', max_length=50),
            preserve_default=False,
        ),
    ]
