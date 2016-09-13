# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ftc_back', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions_attempt',
            name='Team',
            field=models.ForeignKey(to='ftc_back.Teams', blank=True),
        ),
        migrations.AlterField(
            model_name='questions_attempt',
            name='ques_id',
            field=models.ForeignKey(to='ftc_back.Question', blank=True),
        ),
    ]
