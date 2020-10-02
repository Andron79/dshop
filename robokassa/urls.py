from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from robokassa.views import PaymentProcessView, SuccessResultView, FailResultView

app_name = 'robokassa'

urlpatterns = [
    path('robokassa/', PaymentProcessView.as_view(), name='payment_url'),
    path('success/', csrf_exempt(SuccessResultView.as_view()), name='success'),
    path('fail/', csrf_exempt(FailResultView.as_view()), name='fail'),

]
