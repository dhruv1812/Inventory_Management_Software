from django import forms
from .models import *


class productsForm(forms.ModelForm):
    class Meta:
        model = products
        fields = ('product_id', 'name', 'price', 'location', 'count_inventory', 'count_sold')


class customersForm(forms.ModelForm):
    class Meta:
        model = customers
        fields = ('customer_id', 'first_name', 'last_name', 'address','city', 'country', 'postcode')


class ordersForm(forms.ModelForm):
    class Meta:
        model = orders
        fields = ('order_id', 'product_id', 'customer_id', 'order_date', 'delivery_date')