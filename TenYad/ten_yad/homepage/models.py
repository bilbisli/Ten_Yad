from django.db import models
# from ..ten_yad.models import *
# Create your models here.
# import django.contrib.auth
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import HttpResponse
from django.urls import reverse
from django.utils.timezone import now
from django.contrib.auth.models import User

from django.core.validators import MaxValueValidator, MinValueValidator

MIN_STRING = 15
SMALL_STRING = 31
MEDIUM_STRING = 63
LARGE_STRING = 255
XL_STRING = 511
MAX_STRING = 1023


# class Gender(models.Model):
#     gender = models.CharField(max_length=MIN_STRING)
#
#     def __str__(self):
#         return f'{self.gender}'

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications', null=True)
    notification = models.CharField('notification', max_length=LARGE_STRING, blank=True, default='')
    link = models.URLField("link", max_length=LARGE_STRING, blank=True, null=True)
    time = models.DateTimeField('alert_time', default=now)

    def __str__(self):
        return f'{self.notification}, {self.user.profile}, time: {self.time}'


class Profile(models.Model):
    class Gender(models.TextChoices):
        FEMALE = "Female"
        MALE = "Male"
        OTHER = "Other"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField('gender', max_length=MIN_STRING, null=True, blank=True, choices=Gender.choices)
    birth_date = models.DateTimeField('birth date', null=True, blank=True)
    show_email = models.BooleanField(default=False)
    phone = models.CharField(max_length=MIN_STRING, blank=True)
    show_phone = models.BooleanField(default=False)
    telegram = models.CharField(max_length=MIN_STRING, blank=True)
    show_telegram = models.BooleanField(default=False)
    other_contact = models.CharField(max_length=LARGE_STRING, blank=True)
    description = models.TextField(max_length=MAX_STRING, blank=True)
    points = models.IntegerField(default=0)
    rating_sum = models.IntegerField(default=0)
    rating_count = models.IntegerField(default=0)
    unread_notifications = models.IntegerField(default=0)
    is_representative = models.BooleanField(default=False)
    certificate = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.get_username()}'

    def get_email(self):
        return f'{self.user.email}'

    def set_email(self, email):
        self.user.email = email
        self.user.save()

    def set_password(self, password):
        self.user.password = password
        self.user.save()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Category(models.Model):
    name = models.CharField(max_length=MEDIUM_STRING)
    time_signed = models.DateTimeField('time updated', default=now)

    def __str__(self):
        return f'{self.name}'


# class PostType(models.Model):
#     def __str__(self):
#         return f'{self.post_type}'
#
#     post_type = models.CharField(max_length=MIN_STRING)

#
# class PostStatus(models.Model):
#     def __str__(self):
#         return f'{self.post_status}'
#
#     post_status = models.CharField(max_length=MIN_STRING)


class Post(models.Model):
    class PostType(models.TextChoices):
        REQUEST_ASSIST = "Request Assistance"
        OFFER_ASSIST = "Offer Assistance"
        GROUP_ASSIST_REQUEST = "Group Assistance Request"
        GROUP_ASSIST_OFFER = "Group Assistance Offer"

    class PostStatus(models.TextChoices):
        ACTIVE = "Active"
        TRANSACTION = "Transaction"
        ARCHIVE = "Archive"

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField('title', max_length=MEDIUM_STRING)
    category = models.ForeignKey(Category, null=True, related_name='posts', on_delete=models.SET_NULL, blank=True)
    post_type = models.CharField('post type', max_length=MEDIUM_STRING, null=True, choices=PostType.choices,
                                 default=PostType.REQUEST_ASSIST)
    post_status = models.CharField('post status', max_length=MIN_STRING, null=True, choices=PostStatus.choices,
                                   default=PostStatus.ACTIVE)
    time_created = models.DateTimeField('time posted', default=now)
    time_updated_last = models.DateTimeField('last updated', default=now)
    location = models.CharField(max_length=MEDIUM_STRING)
    start_time = models.DateTimeField('relevant from', default=now)
    end_time = models.DateTimeField('relevant until', default=now)
    equipment = models.TextField('equipment details', max_length=LARGE_STRING, blank=True)
    content = models.TextField(max_length=MAX_STRING)
    # reactions = models.ManyToManyField(User, null=True, related_name='reactions', blank=True)
    reactions = models.ManyToManyField(User, related_name='reactions', blank=True)
    approved_reactions = models.ManyToManyField(User, related_name='approved_reactions', blank=True)
    users_assist = models.ManyToManyField(User, related_name='users_assist', blank=True)
    users_to_rate = models.ManyToManyField(User, related_name='users_to_rate', blank=True)
    reacted_user_rate = models.ManyToManyField(User, related_name='reacted_user_rate', blank=True)

    def __str__(self):
        category_print = ''
        if self.category:
            category_print += f'{self.category}'
        else:
            category_print += 'None'
        return f'title: {self.title}, author: {self.user.profile}, category: {category_print}'

    def get_absolute_url(self):
        return reverse('post', args=(str(self.id)))
