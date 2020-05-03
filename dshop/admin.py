from django.contrib import admin
from .models import Category, Product, Article


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'slug', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['published_at', 'product', 'title']
    list_filter = ['published_at', 'product']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Article, ArticleAdmin)
