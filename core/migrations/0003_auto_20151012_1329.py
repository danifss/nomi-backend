# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20151005_0044'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='color',
            field=models.CharField(default='RED', max_length=20, choices=[(b'RED', b'Red'), (b'BLUE', b'Blue'), (b'GREEN', b'Green'), (b'WHITE', b'White'), (b'BLACK', b'Black')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='attribute',
            name='name',
            field=models.CharField(max_length=20, choices=[(b'FACEBOOK', b'Facebook'), (b'PHONE', b'Phone number'), (b'INSTAGRAM', b'Instagram')]),
        ),
    ]
