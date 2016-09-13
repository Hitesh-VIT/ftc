# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_ques', models.IntegerField()),
                ('ques', models.CharField(max_length=100)),
                ('ans', models.CharField(max_length=100)),
                ('strictness', models.CharField(max_length=50)),
                ('newtest', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='questions_attempt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.IntegerField()),
                ('question_attempted', models.IntegerField()),
                ('question_count', models.IntegerField()),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='questions_attempt',
            name='Team',
            field=models.ForeignKey(to='ftc_back.Teams'),
        ),
        migrations.AddField(
            model_name='questions_attempt',
            name='ques_id',
            field=models.ForeignKey(to='ftc_back.Question'),
        ),
    ]
