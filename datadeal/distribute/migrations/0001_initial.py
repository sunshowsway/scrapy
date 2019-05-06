# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-05 09:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('datadeal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=50, verbose_name='uid')),
                ('status', models.BooleanField(default=True, verbose_name='\u662f\u5426\u5f00\u542f')),
            ],
            options={
                'verbose_name': '\u8282\u70b9\u7ba1\u7406',
                'verbose_name_plural': '\u8282\u70b9\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='NodeTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='\u4efb\u52a1\u540d')),
                ('priority', models.IntegerField(default=0, verbose_name='\u4efb\u52a1\u4f18\u5148\u7ea7')),
                ('status', models.IntegerField(choices=[(1, '\u5f85\u91c7\u96c6'), (2, '\u5df2\u5b8c\u6210')], default=1, verbose_name='\u4efb\u52a1\u72b6\u6001')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('get_at', models.DateTimeField(blank=True, null=True, verbose_name='\u4efb\u52a1\u9886\u53d6\u65f6\u95f4')),
                ('over_at', models.DateTimeField(blank=True, null=True, verbose_name='\u4efb\u52a1\u5b8c\u6210\u65f6\u95f4')),
                ('node', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='distribute.Node', verbose_name='\u6267\u884c\u8282\u70b9')),
                ('scrapy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datadeal.scrapyList', verbose_name='\u9879\u76ee')),
                ('urls', models.ManyToManyField(to='datadeal.startUrls', verbose_name='\u722c\u53d6\u94fe\u63a5')),
            ],
            options={
                'verbose_name': '\u4efb\u52a1\u7ba1\u7406',
                'verbose_name_plural': '\u4efb\u52a1\u7ba1\u7406',
            },
        ),
    ]
