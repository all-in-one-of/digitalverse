# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-20 17:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('slug', models.SlugField(default='', max_length=256)),
                ('published', models.BooleanField(default=False)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to='comics/')),
                ('thumbnail', models.ImageField(blank=True, default=None, null=True, upload_to='comics/thumbnails/')),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('score', models.IntegerField(default=0)),
                ('author', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]