from django.urls import path
from .views import OrderCreate, OrderCreated

app_name = 'orders'

urlpatterns = [
    path('create/', OrderCreate.as_view(), name='order_create'),
    path('created/', OrderCreated.as_view(), name='created'),

]