# Generated by Django 3.0.8 on 2021-02-09 08:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('customstaff', '0006_auto_20210117_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='chinesename',
            field=models.CharField(default='', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='incrementall',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 2, 9, 8, 42, 11, 230458, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='enddate',
            field=models.DateField(default=datetime.datetime(2021, 2, 9, 8, 42, 11, 224502, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='endtime',
            field=models.TimeField(default=datetime.datetime(2021, 2, 9, 8, 42, 11, 224526, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='startdate',
            field=models.DateField(default=datetime.datetime(2021, 2, 9, 8, 42, 11, 224442, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='starttime',
            field=models.TimeField(default=datetime.datetime(2021, 2, 9, 8, 42, 11, 224473, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='nonteachingstaffdetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2021, 2, 9, 8, 42, 11, 217136, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='secretarydetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2021, 2, 9, 8, 42, 11, 218508, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='supervisordetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2021, 2, 9, 8, 42, 11, 219843, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='teachingstaffdetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2021, 2, 9, 8, 42, 11, 216073, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='viceprincipaldetail',
            name='firstday',
            field=models.DateField(default=datetime.datetime(2021, 2, 9, 8, 42, 11, 221863, tzinfo=utc)),
        ),
    ]