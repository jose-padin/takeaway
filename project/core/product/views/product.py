from django.views.generic.list import ListView
from django.shortcuts import render

from ..forms.product import ProductForm
from ..models.product import Product


class ProductListView(ListView):
    template_name = 'product/list.html'
    queryset = Product.objects.all()
    context_object_name = 'products'