# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ftc_back', '0002_auto_20160912_0229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='newtest',
        ),
        migrations.AddField(
            model_name='question',
            name='level',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='teams',
            name='level',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='teams',
            name='question_attempted',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='teams',
            name='question_count',
            field=models.IntegerField(default=0),
        ),
    ]
