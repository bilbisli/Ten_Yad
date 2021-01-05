# Generated by Django 3.1.3 on 2020-12-26 15:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('homepage', '0030_auto_20201225_2326'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='users_assist',
            field=models.ManyToManyField(blank=True, related_name='users_assist', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_status',
            field=models.CharField(default='1', max_length=15, null=True, verbose_name='post status'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_type',
            field=models.CharField(default='1', max_length=15, null=True, verbose_name='post type'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=63, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('1', 'Female'), ('2', 'Male'), ('3', 'Other')], max_length=15, null=True, verbose_name='gender'),
        ),
        migrations.DeleteModel(
            name='Gender',
        ),
        migrations.DeleteModel(
            name='PostStatus',
        ),
        migrations.DeleteModel(
            name='PostType',
        ),
    ]
