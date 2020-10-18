from django.views import View

from django.shortcuts import render

from .models.cart import Cart
from .forms.cart import CartForm

TEMPLATE_PATH = '/cart'


class CartView(View):
    form_class = CartForm


    def get(self, request, *args, **kwargs):
        return render(request, f'{TEMPLATE_PATH}/list.html', {})

