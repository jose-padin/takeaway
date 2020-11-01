from django.views.generic.list import ListView
from django.shortcuts import render

from ..forms.product import ProductForm
from ..models.product import Product

TEMPLATE = 'product'


class ProductListView(ListView):
    model = Product

    # context_object_name = 'products'


    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        return render(request, f'{TEMPLATE}/list.html', {'products': products})
