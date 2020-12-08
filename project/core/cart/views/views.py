# import logging
import sys

from pprint import PrettyPrinter

from django.shortcuts import render, redirect, reverse

from core.product.models import Product

from ..models import Cart

dumper = PrettyPrinter(indent=4, stream=sys.stderr).pprint


def list_view(request):
    template = 'cart/list.html'
    cart = Cart(request.session)
    items = cart.items
    return render(request, template, {
        'cart': cart,
        'items': items
    })

def add(request, product_id):
    """Add a product to the cart."""
    product = Product.objects.get(id=product_id)
    company_id = product.company.id
    cart = Cart(request.session)
    cart.add(product)
    return redirect('company:detail', company_id)

def clear(request, company_id, **kwargs):
    # company_id = kwargs['company_id']
    cart = Cart(request.session)
    cart.clear()
    return redirect('company:detail', company_id)

def checkout(request):
    template = 'cart/checkout.html'
    
    return render(request, template)