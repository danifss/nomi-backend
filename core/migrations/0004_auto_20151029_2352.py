# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20151012_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribute',
            name='name',
            field=models.CharField(max_length=20, choices=[(b'FACEBOOK', b'Facebook'), (b'NUMBER', b'Phone number'), (b'INSTAGRAM', b'Instagram'), (b'EMAIL', b'E-mail'), (b'LINKEDIN', b'LinkedIn'), (b'GOOGLE', b'Google'), (b'TWITTER', b'Twitter')]),
        ),
    ]
