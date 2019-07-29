import json
from django.shortcuts import render


def index(request):
    context = {
        'page_title': 'geekshop',
    }
    return render(request, 'mainapp/index.html', context)


def contact(request):
    locations = [
        {
            'city': 'One',
            'phone': '+7-900-800-70-60',
            'email': 'info@geekshop.inbox',
            'address': 'address Street 1',
        },
        {
            'city': 'Two',
            'phone': '+7-800-700-60-50',
            'email': 'info@geekshop.inbox',
            'address': 'address Street 2',
        },
        {
            'city': 'Three',
            'phone': '+7-700-600-50-40',
            'email': 'info@geekshop.inbox',
            'address': 'address Street 3',
        },
    ]

    # with open('geekshop/locations.json', 'w', encoding='utf-8') as f:
    #     json.dump(locations, f)

    # with open('geekshop/locations.json', 'r', encoding='utf-8') as f:
    #     locations = json.load(f)

    context = {
        'page_title': 'contact',
        'locations': locations,
    }
    return render(request, 'mainapp/contact.html', context)


def products(request):
    context = {
        'page_title': 'products',
    }
    return render(request, 'mainapp/products.html', context)
