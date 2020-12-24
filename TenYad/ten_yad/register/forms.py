from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

MIN_STRING = 15


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=MIN_STRING, required=True)
    last_name = forms.CharField(max_length=MIN_STRING, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "first_name", "last_name"]
