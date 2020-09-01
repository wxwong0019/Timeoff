# Generated by Django 3.0.8 on 2020-08-30 08:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('customstaff', '0020_auto_20200829_1414'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supervisordetail',
            name='annualleave',
        ),
        migrations.RemoveField(
            model_name='viceprincipaldetail',
            name='annualleave',
        ),
        migrations.AddField(
            model_name='supervisordetail',
            name='casualleave',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3, verbose_name='Casual Leave Available Days'),
        ),
        migrations.AddField(
            model_name='viceprincipaldetail',
            name='casualleave',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3, verbose_name='Casual Leave Available Days'),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='enddate',
            field=models.DateField(default=datetime.datetime(2020, 8, 30, 8, 20, 23, 974884, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='endtime',
            field=models.TimeField(default=datetime.datetime(2020, 8, 30, 8, 20, 23, 974901, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='startdate',
            field=models.DateField(default=datetime.datetime(2020, 8, 30, 8, 20, 23, 974841, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='starttime',
            field=models.TimeField(default=datetime.datetime(2020, 8, 30, 8, 20, 23, 974863, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='nonteachingstaffdetail',
            name='annualleave',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=2, verbose_name='Annual Leave Available Days'),
        ),
        migrations.AlterField(
            model_name='nonteachingstaffdetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2020, 8, 30, 8, 20, 23, 971683, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='supervisordetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2020, 8, 30, 8, 20, 23, 972199, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='teachingstaffdetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2020, 8, 30, 8, 20, 23, 971055, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='viceprincipaldetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2020, 8, 30, 8, 20, 23, 973284, tzinfo=utc)),
        ),
    ]
