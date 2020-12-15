# Generated by Django 3.1.3 on 2020-11-28 09:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_auto_20201128_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='time_signed',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 28, 9, 49, 45, 48672, tzinfo=utc), verbose_name='time updated'),
        ),
        migrations.AlterField(
            model_name='post',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 28, 9, 49, 45, 48672, tzinfo=utc), verbose_name='timeframe relevancy end'),
        ),
        migrations.AlterField(
            model_name='post',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 28, 9, 49, 45, 48672, tzinfo=utc), verbose_name='timeframe relevancy start'),
        ),
        migrations.AlterField(
            model_name='post',
            name='time_signed',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 28, 9, 49, 45, 48672, tzinfo=utc), verbose_name='time posted'),
        ),
        migrations.AlterField(
            model_name='post',
            name='time_updated_last',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 28, 9, 49, 45, 48672, tzinfo=utc), verbose_name='last updated'),
        ),
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 28, 9, 49, 44, 986173, tzinfo=utc), verbose_name='birth date'),
        ),
        migrations.AlterField(
            model_name='user',
            name='time_signed',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 28, 9, 49, 44, 986173, tzinfo=utc), verbose_name='sign up time'),
        ),
    ]