from django.urls import path
from dshop import views
from dshop.views import ProductDetail # CategoryView

app_name = 'dshop'

urlpatterns = [
    # path('product_list/', CategoryView.as_view(), name='product_list'),
    path('product_list/', views.product_list, name='product_list'),
    path('product/<slug:slug>/', ProductDetail.as_view(), name='product_detail'),
    # path('<slug:slug>/', CategoryView.as_view(), name='product_list_by_category'),
    path('<slug>/', views.product_list, name='product_list_by_category'),

]
