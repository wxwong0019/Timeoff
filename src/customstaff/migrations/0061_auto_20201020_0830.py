# Generated by Django 3.0.8 on 2020-10-20 08:30

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('customstaff', '0060_auto_20201019_0857'),
    ]

    operations = [
        migrations.AddField(
            model_name='nonteachingstaffdetail',
            name='maxannualleave',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=4, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Max. Annual Leave'),
        ),
        migrations.AddField(
            model_name='nonteachingstaffdetail',
            name='maxsickleave',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=4, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(128)], verbose_name='Max. Sick Leave'),
        ),
        migrations.AddField(
            model_name='supervisordetail',
            name='maxsickleave',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=4, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(168)], verbose_name='Max. Sick Leave'),
        ),
        migrations.AddField(
            model_name='teachingstaffdetail',
            name='maxsickleave',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=4, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(168)], verbose_name='Max. Sick Leave'),
        ),
        migrations.AddField(
            model_name='viceprincipaldetail',
            name='maxsickleave',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=4, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(168)], verbose_name='Max. Sick Leave'),
        ),
        migrations.AlterField(
            model_name='incrementall',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2020, 10, 20, 8, 30, 0, 121978, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='enddate',
            field=models.DateField(default=datetime.datetime(2020, 10, 20, 8, 30, 0, 119260, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='endtime',
            field=models.TimeField(default=datetime.datetime(2020, 10, 20, 8, 30, 0, 119283, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='startdate',
            field=models.DateField(default=datetime.datetime(2020, 10, 20, 8, 30, 0, 119201, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='starttime',
            field=models.TimeField(default=datetime.datetime(2020, 10, 20, 8, 30, 0, 119231, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='nonteachingstaffdetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2020, 10, 20, 8, 30, 0, 114459, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='nonteachingstaffdetail',
            name='sickleave',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=4, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)], verbose_name='Sick Leave Available Days'),
        ),
        migrations.AlterField(
            model_name='supervisordetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2020, 10, 20, 8, 30, 0, 115310, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='teachingstaffdetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2020, 10, 20, 8, 30, 0, 113336, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='viceprincipaldetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2020, 10, 20, 8, 30, 0, 116989, tzinfo=utc)),
        ),
    ]
