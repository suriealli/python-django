# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_auto_20160114_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bbs',
            name='ranking',
            field=models.CharField(max_length=100),
        ),
    ]
