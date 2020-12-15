# Generated by Django 3.1.3 on 2020-11-29 23:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0016_auto_20201130_0058'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posttype',
            old_name='assist_offers',
            new_name='post_type',
        ),
        migrations.RemoveField(
            model_name='posttype',
            name='assist_requests',
        ),
        migrations.AlterField(
            model_name='category',
            name='time_signed',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 29, 23, 3, 34, 217416, tzinfo=utc), verbose_name='time updated'),
        ),
        migrations.AlterField(
            model_name='post',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 29, 23, 3, 34, 217416, tzinfo=utc), verbose_name='timeframe relevancy end'),
        ),
        migrations.AlterField(
            model_name='post',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 29, 23, 3, 34, 217416, tzinfo=utc), verbose_name='timeframe relevancy start'),
        ),
        migrations.AlterField(
            model_name='post',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 29, 23, 3, 34, 217416, tzinfo=utc), verbose_name='time posted'),
        ),
        migrations.AlterField(
            model_name='post',
            name='time_updated_last',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 29, 23, 3, 34, 217416, tzinfo=utc), verbose_name='last updated'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 29, 23, 3, 34, 216417, tzinfo=utc), verbose_name='birth date'),
        ),
    ]
