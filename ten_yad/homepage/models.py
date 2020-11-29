from django.db import models
# from ..ten_yad.models import *
# Create your models here.
# import django.contrib.auth
from django.utils.timezone import now

MIN_STRING = 15
SMALL_STRING = 31
MEDIUM_STRING = 63
LARGE_STRING = 255
XL_STRING = 511
MAX_STRING = 1023


class User(models.Model):
    def __str__(self):
        return f'{self.name} {self.last_name}'

    username = models.CharField(max_length=MIN_STRING)
    password = models.CharField(max_length=SMALL_STRING)
    time_registered = models.DateTimeField('registered time', default=now())
    name = models.CharField(max_length=MIN_STRING)
    last_name = models.CharField(max_length=MIN_STRING)
    birth_date = models.DateTimeField('birth date', default=now())
    email = models.EmailField
    show_email = models.BooleanField(default=False)
    phone = models.CharField(max_length=MIN_STRING)
    show_phone = models.BooleanField(default=False)
    telegram = models.CharField(max_length=MIN_STRING)
    show_telegram = models.BooleanField(default=False)
    other_contact = models.CharField(max_length=LARGE_STRING)
    description = models.CharField(max_length=MAX_STRING)
    points = models.IntegerField(default=0)


class Category(models.Model):
    def __str__(self):
        return f'{self.name}'
    name = models.CharField(max_length=MEDIUM_STRING)
    time_signed = models.DateTimeField('time updated', default=now())


class Post(models.Model):
    def __str__(self):
        category_print = ''
        if self.category:
            category_print += f', {self.category}'
        return f'title: {self.title}, author: {self.user}{category_print}'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=MEDIUM_STRING)
    category = models.ForeignKey(Category, null=True, related_name='posts', on_delete=models.SET_NULL)
    time_signed = models.DateTimeField('time posted', default=now())
    time_updated_last = models.DateTimeField('last updated', default=now())
    location = models.CharField(max_length=MEDIUM_STRING)
    start_time = models.DateTimeField('timeframe relevancy start', default=now())
    end_time = models.DateTimeField('timeframe relevancy end', default=now())
    equipment = models.CharField(max_length=LARGE_STRING)
    content = models.CharField(max_length=MAX_STRING)
    status = models.CharField(max_length=MIN_STRING)
