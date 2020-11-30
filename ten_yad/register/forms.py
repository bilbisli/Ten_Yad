from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.utils.timezone import now

MIN_STRING = 15
SMALL_STRING = 31
MEDIUM_STRING = 63
LARGE_STRING = 255
XL_STRING = 511
MAX_STRING = 1023


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=MIN_STRING)
    last_name = forms.CharField(max_length=MIN_STRING)
    email = forms.EmailField

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "first_name", "last_name"]

    """
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
    """