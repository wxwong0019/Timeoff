# Generated by Django 3.0.8 on 2020-08-24 12:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('customstaff', '0005_auto_20200818_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaveapplication',
            name='secondcomment',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='leaveapplication',
            name='secondstatus',
            field=models.CharField(choices=[('Pending', 'pending'), ('Approved', 'approved'), ('Denied', 'denied')], default='Pending', max_length=10),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='enddate',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 24, 12, 27, 49, 578108, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='startdate',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 24, 12, 27, 49, 578083, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='nonteachingstaffdetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2020, 8, 24, 12, 27, 49, 576406, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='supervisordetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2020, 8, 24, 12, 27, 49, 577003, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='teachingstaffdetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2020, 8, 24, 12, 27, 49, 575824, tzinfo=utc)),
        ),
    ]
