# Generated by Django 3.0.8 on 2020-10-22 02:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Timeoff', '0153_auto_20201022_0203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeoff',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 10, 22, 2, 23, 32, 675930, tzinfo=utc)),
        ),
    ]