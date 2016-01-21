# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20160114_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bbs_user',
            name='signature',
            field=models.CharField(default=b'This guy is too lazy to writing something', max_length=128),
        ),
    ]
