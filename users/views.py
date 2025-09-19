# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .models import CustomUser


def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Muvaffaqiyatli ro‘yxatdan o‘tdingiz!")
            return redirect("dashboard:home")
    else:
        form = CustomUserCreationForm()
    return render(request, "users/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Tizimga muvaffaqiyatli kirdingiz!")
            return redirect("dashboard:home")
    else:
        form = CustomAuthenticationForm()
    return render(request, "users/login.html", {"form": form})


def logout_view(request):
    logout(request)
    messages.info(request, "Siz tizimdan chiqdingiz.")
    return redirect("users:login")


@login_required
def profile_view(request):
    return render(request, "users/profile.html", {"user": request.user})