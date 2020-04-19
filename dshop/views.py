from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Product, Category


def index(request):
    template = 'dshop/index.html'
    return render(request, template)


def product_list(request, category_slug=None):
    template = 'dshop/smartphones.html'
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, template,
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id=1, slug=None):
    template = 'dshop/phone.html'
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    return render(request, template,
                  {'product': product})
