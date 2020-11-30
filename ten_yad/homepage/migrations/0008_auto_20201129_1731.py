# Generated by Django 3.1.3 on 2020-11-29 15:31

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('homepage', '0007_auto_20201128_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='time_signed',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 29, 15, 31, 53, 674029, tzinfo=utc), verbose_name='time updated'),
        ),
        migrations.AlterField(
            model_name='post',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 29, 15, 31, 53, 674029, tzinfo=utc), verbose_name='timeframe relevancy end'),
        ),
        migrations.AlterField(
            model_name='post',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 29, 15, 31, 53, 674029, tzinfo=utc), verbose_name='timeframe relevancy start'),
        ),
        migrations.AlterField(
            model_name='post',
            name='time_signed',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 29, 15, 31, 53, 674029, tzinfo=utc), verbose_name='time posted'),
        ),
        migrations.AlterField(
            model_name='post',
            name='time_updated_last',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 29, 15, 31, 53, 674029, tzinfo=utc), verbose_name='last updated'),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateTimeField(default=datetime.datetime(2020, 11, 29, 15, 31, 53, 674029, tzinfo=utc), verbose_name='birth date')),
                ('show_email', models.BooleanField(default=False)),
                ('phone', models.CharField(max_length=15)),
                ('show_phone', models.BooleanField(default=False)),
                ('telegram', models.CharField(max_length=15)),
                ('show_telegram', models.BooleanField(default=False)),
                ('other_contact', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=1023)),
                ('points', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.profile'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]