# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0044_auto_20150322_2034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='slug',
        ),
    ]
