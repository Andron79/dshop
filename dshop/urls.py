from django.urls import path
from dshop import views

app_name = 'dshop'

urlpatterns = [
    path('', views.index, name='index'),
    path('product_list/', views.product_list, name='product_list'),
    path('product/<slug>/', views.product_detail, name='product_detail'),
    path('<slug>/', views.product_list, name='product_list_by_category'),
    #path('articles_list/', views.articles_list, name='articles_list'),
    # path('post/', views.post, name='post'),

]
