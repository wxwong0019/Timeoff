# Generated by Django 3.0.8 on 2020-08-26 09:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Timeoff', '0101_auto_20200826_0809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeoff',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 8, 26, 9, 5, 4, 265166, tzinfo=utc)),
        ),
    ]
