# Generated by Django 3.0.8 on 2021-01-17 08:13

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('customstaff', '0004_auto_20210114_2215'),
    ]

    operations = [
        migrations.AddField(
            model_name='supervisordetail',
            name='annualleave',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(20)], verbose_name='Annual Leave Balance'),
        ),
        migrations.AddField(
            model_name='supervisordetail',
            name='compensatedleave',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=4, verbose_name='Compensated Leave Available (Hours)'),
        ),
        migrations.AddField(
            model_name='supervisordetail',
            name='is_nonteacher',
            field=models.BooleanField(default=False, verbose_name='Non teaching staff status'),
        ),
        migrations.AddField(
            model_name='supervisordetail',
            name='maxannualleave',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=4, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Max. Annual Leave'),
        ),
        migrations.AddField(
            model_name='supervisordetail',
            name='ratio',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=4, verbose_name='Non-Teaching Ratio (100% nonteaching = 1)'),
        ),
        migrations.AlterField(
            model_name='incrementall',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 1, 17, 8, 13, 53, 879244, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='enddate',
            field=models.DateField(default=datetime.datetime(2021, 1, 17, 8, 13, 53, 874631, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='endtime',
            field=models.TimeField(default=datetime.datetime(2021, 1, 17, 8, 13, 53, 874650, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='startdate',
            field=models.DateField(default=datetime.datetime(2021, 1, 17, 8, 13, 53, 874585, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='starttime',
            field=models.TimeField(default=datetime.datetime(2021, 1, 17, 8, 13, 53, 874609, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='nonteachingstaffdetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2021, 1, 17, 8, 13, 53, 869520, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='secretarydetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2021, 1, 17, 8, 13, 53, 870412, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='supervisordetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2021, 1, 17, 8, 13, 53, 871195, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='supervisordetail',
            name='is_teacher',
            field=models.BooleanField(default=False, verbose_name='Teacher status'),
        ),
        migrations.AlterField(
            model_name='teachingstaffdetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2021, 1, 17, 8, 13, 53, 868738, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='viceprincipaldetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2021, 1, 17, 8, 13, 53, 872623, tzinfo=utc)),
        ),
    ]