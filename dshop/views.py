from django.shortcuts import render, get_object_or_404
from .models import Product, Category, Article
from cart.forms import CartAddProductForm
from django.views.generic import ListView, DetailView, FormView


class IndexView(ListView):
    template_name = 'dshop/index.html'
    queryset = Article.objects.all().order_by('published_at')
    context_object_name = 'articles'


# class CategoryView(ListView):
#
#     model = Category
#     slug_field = 'pk'
#     products = Product.objects.filter(available=True)
#     category = get_object_or_404(Category, slug=slug_field)
#     template_name = 'dshop/product/list.html'
#
#     def get_queryset(self):
#         query_set = self.model.objects.filter(category=self.kwargs.get('category'))
#         return query_set
#     # queryset = Product.objects.filter(available=True).filter(category__in=category.get_descendants(include_self=True))
#     context_object_name = 'products'
#     # def get_object(self, queryset=queryset):
#     #     slug = self.kwargs.get(self.slug_url_kwarg, None)
#     #     return queryset.get(slug=slug)
#     # category = get_object_or_404(Category, slug=slug)
#     # queryset = Product.objects.filter(available=True) #.filter(category__in=category.get_descendants(include_self=True))


def product_list(request, slug='root'):
    template = 'dshop/product/list.html'
    products = Product.objects.filter(available=True)
    category = get_object_or_404(Category, slug=slug)
    products = products.filter(category__in=category.get_descendants(include_self=True))
    return render(request, template,
                  {'category': category,
                   'products': products})


class ProductDetail(FormView, DetailView):
    model = Product
    template_name = 'dshop/product/detail.html'
    form_class = CartAddProductForm
    queryset = Product.objects.filter(available=True)
    context_object_name = 'product'


class ArticleView(ListView):
    template_name = 'dshop/articles_list.html'
    queryset = Article.objects.all().order_by('published_at')
    context_object_name = 'articles'


class ArticleDetail(DetailView):
    model = Article
    template_name = 'dshop/article_detail.html'
    context_object_name = 'article'
