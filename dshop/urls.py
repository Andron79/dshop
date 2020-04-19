# from django.conf.urls import url

from django.urls import path

from dshop import views

app_name = 'dshop'

urlpatterns = [
    path('product_list/', views.product_list, name='product_list'),
    path('product_detail/', views.product_detail, name='product_detail'),

]
