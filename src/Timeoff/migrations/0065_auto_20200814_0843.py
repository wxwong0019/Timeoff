# Generated by Django 3.0.8 on 2020-08-14 08:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Timeoff', '0064_auto_20200814_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeoff',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 8, 14, 8, 43, 22, 481892, tzinfo=utc)),
        ),
    ]