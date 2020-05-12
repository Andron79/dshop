from django.shortcuts import render
from dshop.models import Category
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    categories = Category.objects.all()
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # очистка корзины
            cart.clear()
            return render(request, 'orders/created.html',
                          {'order': order,
                           'categories': categories})
    else:
        form = OrderCreateForm
    return render(request, 'orders/create.html',
                  {'cart': cart,
                   'form': form,
                   'categories': categories})
