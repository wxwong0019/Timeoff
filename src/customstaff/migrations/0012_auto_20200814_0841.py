# Generated by Django 3.0.8 on 2020-08-14 08:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('customstaff', '0011_auto_20200814_0823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaveapplication',
            name='enddate',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 14, 8, 41, 42, 704488, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='firstcomment',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='startdate',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 14, 8, 41, 42, 704463, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='nonteachingstaffmore',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2020, 8, 14, 8, 41, 42, 703945, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='teachingstaffmore',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2020, 8, 14, 8, 41, 42, 703143, tzinfo=utc)),
        ),
    ]
