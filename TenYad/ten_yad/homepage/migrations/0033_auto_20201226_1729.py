# Generated by Django 3.1.3 on 2020-12-26 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0032_auto_20201226_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_type',
            field=models.CharField(choices=[('1', 'Request Assistance'), ('2', 'Offer Assistance'), ('3', 'Group Assistance Request'), ('4', 'Group Assistance Offer')], default='1', max_length=15, null=True, verbose_name='post type'),
        ),
    ]
