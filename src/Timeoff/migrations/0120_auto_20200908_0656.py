# Generated by Django 3.0.8 on 2020-09-08 06:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Timeoff', '0119_auto_20200907_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeoff',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 9, 8, 6, 56, 28, 298618, tzinfo=utc)),
        ),
    ]