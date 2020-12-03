from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegisterForm
from django.contrib.auth.decorators import user_passes_test


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/homepage")
    else:
        form = RegisterForm()
    return render(response, 'register/register.html', {'form': form})
