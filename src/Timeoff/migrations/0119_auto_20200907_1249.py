# Generated by Django 3.0.8 on 2020-09-07 12:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Timeoff', '0118_auto_20200907_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeoff',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 9, 7, 12, 49, 10, 1666, tzinfo=utc)),
        ),
    ]