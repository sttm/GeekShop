from django.shortcuts import render


def index(request):
    context = {
        'page_title': 'geekshop',
    }
    return render(request, 'mainapp/index.html', context)


def contact(request):
    context = {
        'page_title': 'contact',
    }
    return render(request, 'mainapp/contact.html', context)


def products(request):
    context = {
        'page_title': 'products',
    }
    return render(request, 'mainapp/products.html', context)
