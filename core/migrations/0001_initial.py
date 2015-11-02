# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, choices=[(b'FACEBOOK', b'Facebook'), (b'NUMBER', b'Phone number'), (b'INSTAGRAM', b'Instagram'), (b'EMAIL', b'E-mail'), (b'LINKEDIN', b'LinkedIn'), (b'GOOGLE', b'Google'), (b'TWITTER', b'Twitter')])),
                ('value', models.CharField(max_length=100)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=20, choices=[(b'RED', b'Red'), (b'BLUE', b'Blue'), (b'GREEN', b'Green'), (b'WHITE', b'White'), (b'BLACK', b'Black')])),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('attributes', models.ManyToManyField(to='core.Attribute', blank=True)),
                ('connections', models.ManyToManyField(to='core.Profile', blank=True)),
            ],
        ),
    ]
