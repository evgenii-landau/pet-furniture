from django.shortcuts import render
from goods.models import Categories


def index(request):
    catigories = Categories.objects.all()
    context = {
        "title": "Home - Главная",
        "content": "Магазин мебели HOME",
        "categories": catigories,
    }

    return render(request, "main/index.html", context=context)


def about(request):
    context = {
        "title": "Home - о нас ",
        "content": "О нас ",
        "text_on_page": "Текст о том какой это классный магазин и какой хороший товар",
    }

    return render(request, "main/about.html", context=context)
