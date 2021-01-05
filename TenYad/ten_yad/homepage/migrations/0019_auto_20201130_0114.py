# Generated by Django 3.1.3 on 2020-11-29 23:14

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0018_auto_20201130_0106'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_status', models.CharField(max_length=15)),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='time_signed',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 29, 23, 14, 24, 770652, tzinfo=utc), verbose_name='time updated'),
        ),
        migrations.AlterField(
            model_name='post',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 29, 23, 14, 24, 772653, tzinfo=utc), verbose_name='timeframe relevancy end'),
        ),
        migrations.AlterField(
            model_name='post',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 29, 23, 14, 24, 772653, tzinfo=utc), verbose_name='timeframe relevancy start'),
        ),
        migrations.AlterField(
            model_name='post',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 29, 23, 14, 24, 771651, tzinfo=utc), verbose_name='time posted'),
        ),
        migrations.AlterField(
            model_name='post',
            name='time_updated_last',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 29, 23, 14, 24, 772653, tzinfo=utc), verbose_name='last updated'),
        ),
        migrations.AlterField(
            model_name='posttype',
            name='post_type',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 29, 23, 14, 24, 769652, tzinfo=utc), verbose_name='birth date'),
        ),
        migrations.AddField(
            model_name='post',
            name='post_status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='homepage.poststatus'),
        ),
    ]
