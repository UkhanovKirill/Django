import json
from django.shortcuts import render
from datetime import datetime
from django.conf import settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from products.models import Product, ProductCategory


def index(request):
    context = {
        'title': 'Geeksop'
    }
    return render(request, 'products/index.html', context)


def products(request, category_id=None, page=1):
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()

    paginator = Paginator(products, 3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    context = {
        'title': 'Geeksop - Каталог',
        'categories': ProductCategory.objects.all(),
        'products': products_paginator,
        'date': datetime.now()
    }
    return render(request, 'products/products.html', context)
