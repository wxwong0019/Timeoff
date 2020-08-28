# Generated by Django 3.0.8 on 2020-08-26 08:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('customstaff', '0014_auto_20200825_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaveapplication',
            name='endtime',
            field=models.TimeField(default=datetime.datetime(2020, 8, 26, 8, 9, 49, 195755, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='leaveapplication',
            name='starttime',
            field=models.TimeField(default=datetime.datetime(2020, 8, 26, 8, 9, 49, 195713, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='enddate',
            field=models.DateField(default=datetime.datetime(2020, 8, 26, 8, 9, 49, 195736, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='startdate',
            field=models.DateField(default=datetime.datetime(2020, 8, 26, 8, 9, 49, 195690, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='nonteachingstaffdetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2020, 8, 26, 8, 9, 49, 192096, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='supervisordetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2020, 8, 26, 8, 9, 49, 192701, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='teachingstaffdetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2020, 8, 26, 8, 9, 49, 191465, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='viceprincipaldetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2020, 8, 26, 8, 9, 49, 194042, tzinfo=utc)),
        ),
    ]
