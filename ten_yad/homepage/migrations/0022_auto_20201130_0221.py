# Generated by Django 3.1.3 on 2020-11-30 00:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0021_auto_20201130_0158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.SmallIntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='time_signed',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 30, 0, 21, 30, 487304, tzinfo=utc), verbose_name='time updated'),
        ),
        migrations.AlterField(
            model_name='post',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 30, 0, 21, 30, 488303, tzinfo=utc), verbose_name='timeframe relevancy end'),
        ),
        migrations.AlterField(
            model_name='post',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 30, 0, 21, 30, 488303, tzinfo=utc), verbose_name='timeframe relevancy start'),
        ),
        migrations.AlterField(
            model_name='post',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 30, 0, 21, 30, 488303, tzinfo=utc), verbose_name='time posted'),
        ),
        migrations.AlterField(
            model_name='post',
            name='time_updated_last',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 30, 0, 21, 30, 488303, tzinfo=utc), verbose_name='last updated'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 30, 0, 21, 30, 487304, tzinfo=utc), verbose_name='birth date'),
        ),
    ]