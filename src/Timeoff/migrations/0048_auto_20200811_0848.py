# Generated by Django 3.0.8 on 2020-08-11 08:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Timeoff', '0047_auto_20200811_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeoff',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 8, 11, 8, 48, 24, 498674, tzinfo=utc)),
        ),
    ]
