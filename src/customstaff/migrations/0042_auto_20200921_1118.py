# Generated by Django 3.0.8 on 2020-09-21 11:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('customstaff', '0041_auto_20200910_0812'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaveapplication',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='incrementall',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2020, 9, 21, 11, 18, 43, 818200, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='enddate',
            field=models.DateField(default=datetime.datetime(2020, 9, 21, 11, 18, 43, 816377, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='endtime',
            field=models.TimeField(default=datetime.datetime(2020, 9, 21, 11, 18, 43, 816399, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='finalduration',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=4, null=True, verbose_name='Modified duration (hr for OT, else use days)'),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='finalstatus',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Denied', 'Denied')], default='Pending', max_length=10, verbose_name='Decision'),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='firststatus',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Denied', 'Denied')], default='Pending', max_length=10, verbose_name='Decision'),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='secondstatus',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Denied', 'Denied')], default='Pending', max_length=10, verbose_name='Decision'),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='startdate',
            field=models.DateField(default=datetime.datetime(2020, 9, 21, 11, 18, 43, 816326, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='starttime',
            field=models.TimeField(default=datetime.datetime(2020, 9, 21, 11, 18, 43, 816353, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='nonteachingstaffdetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2020, 9, 21, 11, 18, 43, 812930, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='supervisordetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2020, 9, 21, 11, 18, 43, 813508, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='teachingstaffdetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2020, 9, 21, 11, 18, 43, 812290, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='viceprincipaldetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2020, 9, 21, 11, 18, 43, 814732, tzinfo=utc)),
        ),
    ]