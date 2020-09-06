# Generated by Django 3.0.8 on 2020-08-29 14:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('customstaff', '0019_auto_20200828_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaveapplication',
            name='enddate',
            field=models.DateField(default=datetime.datetime(2020, 8, 29, 14, 14, 27, 544411, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='endtime',
            field=models.TimeField(default=datetime.datetime(2020, 8, 29, 14, 14, 27, 544428, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='nonteachertimeofftype',
            field=models.CharField(choices=[('Sick Leave', 'Sick Leave'), ('Official Leave', 'Official Leave'), ('Annual Leave', 'Annual Leave'), ('Over Time', 'Over Time'), ('Special Tuberculosis Leave', 'Special Tuberculosis Leave'), ('Maternal Leave', 'Maternal Leave'), ('Paternity Leave', 'Paternity Leave'), ('Jurors or Witnesses', 'Jurors or Witnesses'), ('Others', 'Others')], default='Sick Leave', max_length=100, verbose_name='Non Teacher Type of Leave'),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='startdate',
            field=models.DateField(default=datetime.datetime(2020, 8, 29, 14, 14, 27, 544367, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='starttime',
            field=models.TimeField(default=datetime.datetime(2020, 8, 29, 14, 14, 27, 544390, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='teachertimeofftype',
            field=models.CharField(choices=[('Sick Leave', 'Sick Leave'), ('Official Leave', 'Official Leave'), ('Casual Leave', 'Casual Leave'), ('Special Tuberculosis Leave', 'Special Tuberculosis Leave'), ('Maternal Leave', 'Maternal Leave'), ('Paternity Leave', 'Paternity Leave'), ('Study Leave', 'Study Leave'), ('Jurors or Witnesses', 'Jurors or Witnesses'), ('Leave for Special Events', 'Leave for Special Events'), ('Others', 'Others')], default='Sick Leave', max_length=100, verbose_name='Type of Leave'),
        ),
        migrations.AlterField(
            model_name='nonteachingstaffdetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2020, 8, 29, 14, 14, 27, 541205, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='supervisordetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2020, 8, 29, 14, 14, 27, 541721, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='teachingstaffdetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2020, 8, 29, 14, 14, 27, 540519, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='viceprincipaldetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2020, 8, 29, 14, 14, 27, 542805, tzinfo=utc)),
        ),
    ]