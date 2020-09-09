# Generated by Django 3.0.8 on 2020-09-07 10:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('customstaff', '0029_auto_20200907_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaveapplication',
            name='enddate',
            field=models.DateField(default=datetime.datetime(2020, 9, 7, 10, 21, 19, 497892, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='endtime',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 7, 10, 21, 19, 497911, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='startdate',
            field=models.DateField(default=datetime.datetime(2020, 9, 7, 10, 21, 19, 497844, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='starttime',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 7, 10, 21, 19, 497867, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='nonteachingstaffdetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2020, 9, 7, 10, 21, 19, 494624, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='supervisordetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2020, 9, 7, 10, 21, 19, 495170, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='teachingstaffdetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2020, 9, 7, 10, 21, 19, 494049, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='viceprincipaldetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2020, 9, 7, 10, 21, 19, 496283, tzinfo=utc)),
        ),
    ]