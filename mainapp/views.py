from django.shortcuts import render


def index(request):
    context = {
        'page_title': 'GeekShop',
    }
    return render(request, 'mainapp/index.html', context)


def contact(request):
    context = {
        'page_title': 'Contact',
    }
    return render(request, 'mainapp/contact.html', context)


def products(request):
    context = {
        'page_title': 'Products',
    }
    return render(request, 'mainapp/products.html', context)
