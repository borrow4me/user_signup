# Generated by Django 3.2.7 on 2021-11-17 14:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210812_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='card_month',
            field=models.DateTimeField(default=datetime.date(2021, 11, 17)),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='card_year',
            field=models.DateTimeField(blank=True, default=datetime.date(2021, 11, 17), null=True),
        ),
    ]
