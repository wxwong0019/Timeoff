# Generated by Django 3.0.8 on 2020-11-08 07:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Timeoff', '0162_auto_20201104_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeoff',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 11, 8, 7, 54, 3, 223802, tzinfo=utc)),
        ),
    ]