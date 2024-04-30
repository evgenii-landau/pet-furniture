from calendar import c
from django.shortcuts import render


def login(request):
    context = {"title": "Авторизация"}

    return render(request, "users/login.html", context=context)


def registration(request):
    context = {
        "titlte": "Регистрация",
    }

    return render(request, "users/registration.html", context=context)


def profile(request):
    context = {
        "titlte": "Профиль",
    }

    return render(request, "users/profile.html", context=context)


def logout(request):
    pass
