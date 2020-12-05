from django.db import models
# from ..ten_yad.models import *
# Create your models here.
# import django.contrib.auth
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

MIN_STRING = 15
SMALL_STRING = 31
MEDIUM_STRING = 63
LARGE_STRING = 255
XL_STRING = 511
MAX_STRING = 1023


class Gender(models.Model):
    gender = models.CharField(max_length=MIN_STRING)

    def __str__(self):
        return f'{self.gender}'


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender, null=True, related_name='users', on_delete=models.SET_NULL)
    birth_date = models.DateTimeField('birth date', default=now)
    show_email = models.BooleanField(default=False)
    phone = models.CharField(max_length=MIN_STRING)
    show_phone = models.BooleanField(default=False)
    telegram = models.CharField(max_length=MIN_STRING)
    show_telegram = models.BooleanField(default=False)
    other_contact = models.CharField(max_length=LARGE_STRING)
    description = models.TextField(max_length=MAX_STRING)
    points = models.IntegerField(default=0)
    rating_sum = models.IntegerField(default=0)
    rating_count = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.get_username()}'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Category(models.Model):
    def __str__(self):
        return f'{self.name}'
    name = models.CharField(max_length=MEDIUM_STRING)
    time_signed = models.DateTimeField('time updated', default=now)


class PostType(models.Model):
    def __str__(self):
        return f'{self.post_type}'

    post_type = models.CharField(max_length=MIN_STRING)


class PostStatus(models.Model):
    def __str__(self):
        return f'{self.post_status}'

    post_status = models.CharField(max_length=MIN_STRING)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=MEDIUM_STRING)
    category = models.ForeignKey(Category, null=True, related_name='posts', on_delete=models.SET_NULL)
    post_type = models.ForeignKey(PostType, null=True, related_name='posts', on_delete=models.SET_DEFAULT, default=1)
    post_status = models.ForeignKey(PostStatus, null=True, related_name='posts', on_delete=models.SET_DEFAULT, default=1)
    time_created = models.DateTimeField('time posted', default=now)
    time_updated_last = models.DateTimeField('last updated', default=now)
    location = models.CharField(max_length=MEDIUM_STRING)
    start_time = models.DateTimeField('relevant from', default=now)
    end_time = models.DateTimeField('relevant until', default=now)
    equipment = models.TextField(max_length=LARGE_STRING)
    content = models.TextField(max_length=MAX_STRING)

    def __str__(self):
        category_print = ''
        if self.category:
            category_print += f', {self.category}'
        return f'title: {self.title}, author: {self.user.profile}, category: {category_print}'
