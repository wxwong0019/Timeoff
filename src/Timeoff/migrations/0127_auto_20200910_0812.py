# Generated by Django 3.0.8 on 2020-09-10 08:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Timeoff', '0126_auto_20200910_0416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeoff',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 9, 10, 8, 12, 15, 795289, tzinfo=utc)),
        ),
    ]