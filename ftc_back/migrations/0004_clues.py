# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ftc_back', '0003_auto_20160912_1618'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clues',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clue_id', models.IntegerField()),
                ('clue_lt', models.FloatField()),
                ('clue_ln', models.FloatField()),
                ('clue_question', models.OneToOneField(to='ftc_back.Question')),
            ],
        ),
    ]
