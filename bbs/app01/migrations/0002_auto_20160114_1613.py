# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bbs_user',
            name='signature',
            field=models.CharField(default=b'this gus is too lazy to writing something', max_length=128),
        ),
    ]
