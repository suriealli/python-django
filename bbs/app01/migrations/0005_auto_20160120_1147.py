# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app01', '0004_auto_20160116_1010'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=64)),
                ('summary', models.CharField(max_length=256, null=True, blank=True)),
                ('content', models.TextField()),
                ('view_count', models.IntegerField()),
                ('ranking', models.CharField(max_length=100)),
                ('created_time', models.DateTimeField()),
                ('updated_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_time'],
            },
        ),
        migrations.CreateModel(
            name='ArticleManager',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('signature', models.CharField(default=b'This guy is too lazy to writing something', max_length=128)),
                ('photo', models.ImageField(default=b'up_photo/default.jpg', upload_to=b'up_photo')),
                ('email', models.EmailField(max_length=256, blank=True)),
                ('website', models.URLField(max_length=256, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, blank=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='bbs',
            name='author',
        ),
        migrations.RemoveField(
            model_name='bbs_user',
            name='user',
        ),
        migrations.RemoveField(
            model_name='category',
            name='admin',
        ),
        migrations.DeleteModel(
            name='BBS',
        ),
        migrations.DeleteModel(
            name='BBS_user',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(to='app01.Author'),
        ),
        migrations.AddField(
            model_name='article',
            name='classification',
            field=models.ForeignKey(to='app01.Classification'),
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(to='app01.Tag', blank=True),
        ),
    ]
