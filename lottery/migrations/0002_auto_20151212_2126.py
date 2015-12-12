# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-12 21:26
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='lottery',
            managers=[
                ('open_lotteries', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='lotteryticket',
            unique_together=set([('lottery', 'player')]),
        ),
    ]