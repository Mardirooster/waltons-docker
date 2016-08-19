# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0004_instrument'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Course',
            new_name='Lesson',
        ),
    ]
