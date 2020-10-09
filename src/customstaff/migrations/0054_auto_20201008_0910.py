# Generated by Django 3.0.8 on 2020-10-08 09:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('customstaff', '0053_auto_20201008_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incrementall',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2020, 10, 8, 9, 10, 57, 216338, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='enddate',
            field=models.DateField(default=datetime.datetime(2020, 10, 8, 9, 10, 57, 213917, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='endtime',
            field=models.TimeField(default=datetime.datetime(2020, 10, 8, 9, 10, 57, 213940, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='nonteacherchangetimeofftype',
            field=models.CharField(blank=True, choices=[('Annual Leave', 'Annual Leave'), ('Over Time', 'Over Time'), ('No-Pay Leave', 'No-Pay Leave')], max_length=100, null=True, verbose_name='Change Leave Type'),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='nonteachertimeofftype',
            field=models.CharField(choices=[('Sick Leave', 'Sick Leave'), ('Official Leave (In School)', 'Official Leave (In School)'), ('Official Leave (Outside)', 'Official Leave (Outside)'), ('Annual Leave', 'Annual Leave'), ('Over Time', 'Over Time'), ('Special Tuberculosis Leave', 'Special Tuberculosis Leave'), ('Maternal Leave', 'Maternal Leave'), ('No-Pay Leave', 'No-Pay Leave'), ('Paternity Leave', 'Paternity Leave'), ('Jurors or Witnesses', 'Jurors or Witnesses'), ('Others', 'Others')], default='Sick Leave', max_length=100, verbose_name='Type of Leave'),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='startdate',
            field=models.DateField(default=datetime.datetime(2020, 10, 8, 9, 10, 57, 213863, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='starttime',
            field=models.TimeField(default=datetime.datetime(2020, 10, 8, 9, 10, 57, 213891, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='teacherchangetimeofftype',
            field=models.CharField(blank=True, choices=[('Over Time', 'Casual Leave'), ('No-Pay Leave', 'No-Pay Leave')], max_length=100, null=True, verbose_name='Change Leave Type'),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='teachertimeofftype',
            field=models.CharField(choices=[('Sick Leave', 'Sick Leave'), ('Official Leave (In School)', 'Official Leave (In School)'), ('Official Leave (Outside)', 'Official Leave (Outside)'), ('Casual Leave', 'Casual Leave'), ('Special Tuberculosis Leave', 'Special Tuberculosis Leave'), ('Maternal Leave', 'Maternal Leave'), ('No-Pay Leave', 'No-Pay Leave'), ('Paternity Leave', 'Paternity Leave'), ('Study Leave', 'Study Leave'), ('Jurors or Witnesses', 'Jurors or Witnesses'), ('Leave for Special Events', 'Leave for Special Events'), ('Others', 'Others')], default='Sick Leave', max_length=100, verbose_name='Type of Leave'),
        ),
        migrations.AlterField(
            model_name='nonteachingstaffdetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2020, 10, 8, 9, 10, 57, 209779, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='supervisordetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2020, 10, 8, 9, 10, 57, 210467, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='teachingstaffdetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2020, 10, 8, 9, 10, 57, 209033, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='viceprincipaldetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2020, 10, 8, 9, 10, 57, 211954, tzinfo=utc)),
        ),
    ]
