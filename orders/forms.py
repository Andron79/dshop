from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        # widgets = {'username': forms.HiddenInput()}
        fields = ['first_name', 'last_name', 'email', 'address', 'phone', 'city']
