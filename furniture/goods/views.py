from django.shortcuts import render


def catalog(request):
    context = {
        "tilte": "Каталог",
    }
    return render(request, "goods/catalog.html", context=context)


def product(request):
    context = {
        "tilte": "Товар",
    }
    return render(request, "goods/product.html", context=context)
