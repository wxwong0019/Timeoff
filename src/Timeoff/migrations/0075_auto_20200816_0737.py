# Generated by Django 3.0.8 on 2020-08-16 07:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Timeoff', '0074_auto_20200816_0636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeoff',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 8, 16, 7, 37, 28, 332257, tzinfo=utc)),
        ),
    ]