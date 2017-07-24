# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-24 20:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='jfadmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='jfcompany',
            fields=[
                ('cid', models.CharField(blank=True, default=uuid.uuid4, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(default='company', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='jfuser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phno', models.IntegerField(default=70000000)),
                ('college', models.CharField(default='college', max_length=50)),
                ('nofc', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='usercompanies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.CharField(default='company', max_length=50)),
                ('paid', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to='paid')),
                ('nofp', models.IntegerField(default=0)),
                ('jfcompany', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='register.jfcompany')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.jfuser')),
            ],
        ),
    ]
