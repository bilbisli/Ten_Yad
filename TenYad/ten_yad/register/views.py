from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegisterForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.messages import constants as messages
from .decorators import unauthenticated_user

@user_passes_test(lambda user: not user.is_authenticated)
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            # messages.INFO(response, "Thanks for registering. You are now logged in.")
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(response, new_user)
            return redirect("/")
    else:
        form = RegisterForm()
    return render(response, 'register/register.html', {'form': form})
