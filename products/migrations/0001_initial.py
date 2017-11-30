# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-07 19:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('manufacturers', '0001_initial'),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=10, unique=True, verbose_name='Product code')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='products/image')),
                ('stock', models.PositiveIntegerField()),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.Category')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manufacturers.Manufacturer')),
            ],
        ),
    ]