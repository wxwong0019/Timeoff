# Generated by Django 3.0.8 on 2020-09-28 12:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Timeoff', '0128_auto_20200921_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeoff',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 9, 28, 12, 38, 11, 387296, tzinfo=utc)),
        ),
    ]