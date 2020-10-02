from django.urls import path
from dshop import views
from dshop.views import ProductDetail, ProductListView

app_name = 'dshop'

urlpatterns = [
    # path('product_list/', ProductListView.as_view(), name='product_list'),
    path('product_list/', views.product_list, name='product_list'),
    path('product/<slug:slug>/', ProductDetail.as_view(), name='product_detail'),
    path('<slug>/', views.product_list, name='product_list_by_category'),
    # path('<slug>/', ProductListCategoryView.as_view(), name='product_list_by_category'),

]
