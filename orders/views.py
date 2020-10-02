from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView, TemplateView
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart


class OrderCreate(FormView, CreateView):
    form_class = OrderCreateForm
    model = Order
    template_name = 'orders/create.html'
    success_url = reverse_lazy('orders:created')

    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        form = self.form_class(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if request.user.is_authenticated:
                order.username = request.user
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
        return HttpResponseRedirect(self.success_url)

    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        user = request.user
        data = {}
        if user.is_authenticated:
            data["last_name"] = user.last_name
            data["first_name"] = user.first_name
            data["email"] = user.email
        form = self.form_class(initial=data)
        return render(request, 'orders/create.html',
                      {'cart': cart,
                       'form': form})


class OrderCreated(TemplateView):
    template_name = 'orders/created.html'
    model = Order
    extra_context = {'order': Order.objects.first().id}


