# Generated by Django 3.2.4 on 2021-08-12 01:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='card_month',
            field=models.DateTimeField(default=datetime.date(2021, 8, 12)),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='card_year',
            field=models.DateTimeField(blank=True, default=datetime.date(2021, 8, 12), null=True),
        ),
    ]
