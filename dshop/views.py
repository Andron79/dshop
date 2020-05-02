from django.shortcuts import render, get_object_or_404
from .models import Product, Category, Article


# from django.views.generic import ListView


def index(request):
    template = 'dshop/index.html'
    categories = Category.objects.all()
    # articles = Article.objects.all().order_by('published_at')

    return render(request, template,
                  context={'categories': categories}
                  )


def product_list(request, slug):
    template = 'dshop/product/list.html'
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    category = get_object_or_404(Category, slug=slug)
    products = products.filter(category=category)
    return render(request, template,
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, slug):
    template = 'dshop/product/detail.html'
    product = get_object_or_404(Product,
                                slug=slug,
                                available=True)
    categories = Category.objects.all()
    return render(request, template,
                  {'product': product,
                   'categories': categories})


def articles_list(request):
    print('jjjjjjjjjjjjjjjjjjjjjjjjjjj')
    template = 'dshop/product/articles_list.html'
    categories = Category.objects.all()
    articles = Article.objects.all()
    print(articles)
    return render(request, template,
                  context={
                      'articles': articles,
                      'categories': categories}
                  )

