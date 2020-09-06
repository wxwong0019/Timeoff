# Generated by Django 3.0.8 on 2020-08-30 08:31

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('customstaff', '0023_auto_20200830_0829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaveapplication',
            name='enddate',
            field=models.DateField(default=datetime.datetime(2020, 8, 30, 8, 31, 22, 918769, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='endtime',
            field=models.TimeField(default=datetime.datetime(2020, 8, 30, 8, 31, 22, 918787, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='startdate',
            field=models.DateField(default=datetime.datetime(2020, 8, 30, 8, 31, 22, 918725, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='starttime',
            field=models.TimeField(default=datetime.datetime(2020, 8, 30, 8, 31, 22, 918747, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='nonteachingstaffdetail',
            name='annualleave',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=2, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(20)], verbose_name='Annual Leave Available Days'),
        ),
        migrations.AlterField(
            model_name='nonteachingstaffdetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2020, 8, 30, 8, 31, 22, 915470, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='nonteachingstaffdetail',
            name='sickleave',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=4, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(20)], verbose_name='Sick Leave Available Days'),
        ),
        migrations.AlterField(
            model_name='supervisordetail',
            name='casualleave',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(20)], verbose_name='Casual Leave Available Days'),
        ),
        migrations.AlterField(
            model_name='supervisordetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2020, 8, 30, 8, 31, 22, 916007, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='supervisordetail',
            name='sickleave',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=4, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(20)], verbose_name='Sick Leave Available Days'),
        ),
        migrations.AlterField(
            model_name='teachingstaffdetail',
            name='casualleave',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(20)], verbose_name='Casual Leave Available Days'),
        ),
        migrations.AlterField(
            model_name='teachingstaffdetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2020, 8, 30, 8, 31, 22, 914848, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='teachingstaffdetail',
            name='sickleave',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=4, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(20)], verbose_name='Sick Leave Available Days'),
        ),
        migrations.AlterField(
            model_name='viceprincipaldetail',
            name='casualleave',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(20)], verbose_name='Casual Leave Available Days'),
        ),
        migrations.AlterField(
            model_name='viceprincipaldetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2020, 8, 30, 8, 31, 22, 917140, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='viceprincipaldetail',
            name='sickleave',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=4, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(20)], verbose_name='Sick Leave Available Days'),
        ),
    ]