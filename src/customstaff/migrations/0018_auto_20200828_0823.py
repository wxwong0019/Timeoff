# Generated by Django 3.0.8 on 2020-08-28 08:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('customstaff', '0017_auto_20200826_0906'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaveapplication',
            name='finalduration',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=4, verbose_name='Modified duration (hr for OT, else use days)'),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='enddate',
            field=models.DateField(default=datetime.datetime(2020, 8, 28, 8, 23, 52, 395492, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='endtime',
            field=models.TimeField(default=datetime.datetime(2020, 8, 28, 8, 23, 52, 395511, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='startdate',
            field=models.DateField(default=datetime.datetime(2020, 8, 28, 8, 23, 52, 395437, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='starttime',
            field=models.TimeField(default=datetime.datetime(2020, 8, 28, 8, 23, 52, 395470, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='teachertimeofftype',
            field=models.CharField(choices=[('SL', 'Sick Leave'), ('OL', 'Official Leave'), ('CL', 'Casual Leave'), ('TB', 'Special Tuberculosis Leave'), ('ML', 'Maternal Leave'), ('PL', 'Paternity Leave'), ('ST', 'Study Leave'), ('JK', 'Jurors or Witnesses'), ('LS', 'Leave for Special Events'), ('O', 'Others')], default='SL', max_length=10, verbose_name='Type of Leave'),
        ),
        migrations.AlterField(
            model_name='nonteachingstaffdetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2020, 8, 28, 8, 23, 52, 392221, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='supervisordetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2020, 8, 28, 8, 23, 52, 392738, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='teachingstaffdetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2020, 8, 28, 8, 23, 52, 391575, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='viceprincipaldetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2020, 8, 28, 8, 23, 52, 393846, tzinfo=utc)),
        ),
    ]
