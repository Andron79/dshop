from django.http import response
from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from django.contrib.auth.models import User


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        # user = request.user
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if request.user.is_authenticated:
                order.username = request.user
                # order.first_name = request.user.first_name
                # order.last_name = request.user.last_name
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # очистка корзины
            cart.clear()
            print(request.user.last_name)
            return render(request, 'orders/created.html',
                          {'order': order,
                           'form.first_name': order.first_name,
                           'form.last_name': order.last_name})
    else:
        form = OrderCreateForm
    return render(request, 'orders/create.html',
                  {'cart': cart,
                   'form': form})
