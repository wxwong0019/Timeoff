# Generated by Django 3.0.8 on 2020-08-25 14:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('customstaff', '0013_auto_20200825_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaveapplication',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='enddate',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 25, 14, 14, 31, 797142, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='startdate',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 25, 14, 14, 31, 797116, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='nonteachingstaffdetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2020, 8, 25, 14, 14, 31, 793564, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='supervisordetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2020, 8, 25, 14, 14, 31, 794157, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='teachingstaffdetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2020, 8, 25, 14, 14, 31, 792863, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='viceprincipaldetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2020, 8, 25, 14, 14, 31, 795366, tzinfo=utc)),
        ),
    ]