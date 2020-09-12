# Generated by Django 3.0.8 on 2020-09-10 04:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('customstaff', '0039_auto_20200910_0318'),
    ]

    operations = [
        migrations.AddField(
            model_name='nonteachingstaffdetail',
            name='ratio',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2, verbose_name='Ratio'),
        ),
        migrations.AlterField(
            model_name='incrementall',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2020, 9, 10, 4, 16, 3, 267368, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='enddate',
            field=models.DateField(default=datetime.datetime(2020, 9, 10, 4, 16, 3, 264859, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='endtime',
            field=models.TimeField(default=datetime.datetime(2020, 9, 10, 4, 16, 3, 264890, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='startdate',
            field=models.DateField(default=datetime.datetime(2020, 9, 10, 4, 16, 3, 264778, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='starttime',
            field=models.TimeField(default=datetime.datetime(2020, 9, 10, 4, 16, 3, 264822, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='nonteachingstaffdetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2020, 9, 10, 4, 16, 3, 259851, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='supervisordetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2020, 9, 10, 4, 16, 3, 260434, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='teachingstaffdetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2020, 9, 10, 4, 16, 3, 259218, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='viceprincipaldetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2020, 9, 10, 4, 16, 3, 262146, tzinfo=utc)),
        ),
    ]
