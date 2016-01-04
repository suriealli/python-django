# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BBS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=64)),
                ('summary', models.CharField(max_length=256, null=True, blank=True)),
                ('content', models.TextField()),
                ('view_count', models.IntegerField()),
                ('ranking', models.ImageField(upload_to=b'')),
                ('created_at', models.DateTimeField()),
                ('update_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='BBS_user',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('signature', models.CharField(default=b'111', max_length=128)),
                ('photo', models.ImageField(default=b'up_photo/default.jpg', upload_to=b'up_photo')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=32)),
                ('admin', models.ForeignKey(to='app01.BBS_user')),
            ],
        ),
        migrations.AddField(
            model_name='bbs',
            name='author',
            field=models.ForeignKey(to='app01.BBS_user'),
        ),
    ]
