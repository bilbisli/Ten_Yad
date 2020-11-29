# from django.db import models
#
# # Create your models here.
# # class Post(models.Model):
#
# MIN_STRING = 15
# SMALL_STRING = 31
# MEDIUM_STRING = 63
# LARGE_STRING = 255
# XL_STRING = 511
# MAX_STRING = 1023
#
#
# class User(models.Model):
#     username = models.CharField(max_length=MIN_STRING)
#     password = models.CharField(max_length=SMALL_STRING)
#     time_signed = models.DateTimeField
#     name = models.CharField(max_length=MIN_STRING)
#     last_name = models.CharField(max_length=MIN_STRING)
#     birth_date = models.DateTimeField
#     email = models.EmailField
#     phone = models.CharField(max_length=MIN_STRING)
#     show_phone = models.BooleanField
#     telegram = models.CharField(max_length=MIN_STRING)
#     show_telegram = models.BooleanField
#     other_contact = models.CharField(max_length=LARGE_STRING)
#     description = models.CharField(max_length=MAX_STRING)
#     points = models.IntegerField
#
#
# class Category(models.Model):
#     name = models.CharField(max_length=MEDIUM_STRING)
#     time_signed = models.DateTimeField
