import json
from django.shortcuts import render
from datetime import datetime
from django.conf import settings


def index(request):
    context = {
        'title': 'Geeksop'
    }
    return render(request, 'products/index.html', context)


def products(request):
    file_path = settings.BASE_DIR / 'products/fixtures/goods.json'
    context = {
        'title': 'Geeksop - Каталог',
        'products': json.load(open(file_path, encoding='utf-8')),
        'date': datetime.now()
    }
    return render(request, 'products/products.html', context)
