from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {"title": "Home", "content": "Main page shop - Home", 'categories': ['Armchair', 'Chair', 'Bed']}

    return render(request, "main/index.html", context=context)


def about(request):
    return HttpResponse("About page")
