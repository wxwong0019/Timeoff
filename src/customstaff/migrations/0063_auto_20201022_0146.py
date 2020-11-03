# Generated by Django 3.0.8 on 2020-10-22 01:46

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('customstaff', '0062_auto_20201020_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incrementall',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2020, 10, 22, 1, 46, 4, 715082, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='enddate',
            field=models.DateField(default=datetime.datetime(2020, 10, 22, 1, 46, 4, 711990, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='endtime',
            field=models.TimeField(default=datetime.datetime(2020, 10, 22, 1, 46, 4, 712009, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='nonteachertimeofftype',
            field=models.CharField(choices=[('Sick Leave', 'Sick Leave'), ('Official Leave (In School)', 'Official Leave (In School)'), ('Official Leave (Outside)', 'Official Leave (Outside)'), ('Annual Leave', 'Annual Leave'), ('Over Time', 'Over Time'), ('Special Tuberculosis Leave', 'Special Tuberculosis Leave'), ('Maternal Leave', 'Maternal Leave'), ('No-Pay Leave', 'No-Pay Leave'), ('Paternity Leave', 'Paternity Leave'), ('Jurors or Witnesses', 'Jurors or Witnesses'), ('Others', 'Others')], default=None, max_length=100, verbose_name='Type of Leave'),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='startdate',
            field=models.DateField(default=datetime.datetime(2020, 10, 22, 1, 46, 4, 711938, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='starttime',
            field=models.TimeField(default=datetime.datetime(2020, 10, 22, 1, 46, 4, 711963, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='teachertimeofftype',
            field=models.CharField(choices=[('Sick Leave', 'Sick Leave'), ('Official Leave (In School)', 'Official Leave (In School)'), ('Official Leave (Outside)', 'Official Leave (Outside)'), ('Casual Leave', 'Casual Leave'), ('Special Tuberculosis Leave', 'Special Tuberculosis Leave'), ('Maternal Leave', 'Maternal Leave'), ('No-Pay Leave', 'No-Pay Leave'), ('Paternity Leave', 'Paternity Leave'), ('Study Leave', 'Study Leave'), ('Jurors or Witnesses', 'Jurors or Witnesses'), ('Leave for Special Events', 'Leave for Special Events'), ('Others', 'Others')], default=None, max_length=100, verbose_name='Type of Leave'),
        ),
        migrations.AlterField(
            model_name='nonteachingstaffdetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2020, 10, 22, 1, 46, 4, 708128, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='supervisordetail',
            name='casualleave',
            field=models.DecimalField(decimal_places=2, default=2, max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(20)], verbose_name='Casual Leave Available Days'),
        ),
        migrations.AlterField(
            model_name='supervisordetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2020, 10, 22, 1, 46, 4, 708818, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='teachingstaffdetail',
            name='casualleave',
            field=models.DecimalField(decimal_places=2, default=2, max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(20)], verbose_name='Casual Leave Available Days'),
        ),
        migrations.AlterField(
            model_name='teachingstaffdetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2020, 10, 22, 1, 46, 4, 707474, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='viceprincipaldetail',
            name='casualleave',
            field=models.DecimalField(decimal_places=2, default=2, max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(20)], verbose_name='Casual Leave Available Days'),
        ),
        migrations.AlterField(
            model_name='viceprincipaldetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2020, 10, 22, 1, 46, 4, 710050, tzinfo=utc)),
        ),
    ]