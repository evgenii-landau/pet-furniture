from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {"title": "Home - Главная", "content": "Магазин мебели HOME"}

    return render(request, "main/index.html", context=context)


def about(request):
    context = {
        "title": "Home - о нас ",
        "content": "О нас ",
        "text_on_page": "Текст о том какой это классный магазин и какой хороший товар",
    }

    return render(request, "main/about.html", context=context)
