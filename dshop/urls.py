from django.conf.urls import url

from django.urls import path
from django.conf.urls.static import static
from dshop import views

app_name = 'dshop'

urlpatterns = [
    path('', views.index, name='index'),
    path('product_list/', views.product_list, name='product_list'),
    #path('<slug>/$', views.product_detail, name='product_detail'),
    #path('product_list/''<slug>/$', views.product_list, name='product_list'),
    #path('<slug>/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        views.product_detail,
        name='product_detail'),

]
