from django.http import HttpResponseRedirect
from django.views.generic.base import View, TemplateView

from orders.models import Order
from robokassa.utils import get_payment_url


class PaymentProcessView(View):

    def post(self, request):
        if request.method == "POST":
            order_data = Order.objects.first()
            url = get_payment_url(order_data.id, order_data.get_total_cost(), 'Оплата заказа')
        return HttpResponseRedirect(url)


class SuccessResultView(TemplateView):
    template_name = 'robokassa/payment_success.html'
    order_data = Order.objects.first()
    order_data.paid = True
    order_data.save()


class FailResultView(TemplateView):
    template_name = 'robokassa/payment_fail.html'
