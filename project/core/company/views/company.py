import sys

from pprint import PrettyPrinter

from django.shortcuts import render

from core.cart.models import Cart
from core.product.models import Product, Category, ProductCategory

from ..forms.company import CompanyForm
from ..models import Company

dumper = PrettyPrinter(indent=4, stream=sys.stderr).pprint


def company_list_view(request):
    template = 'company/list.html'
    companies = Company.objects.all()
    categories = Category.objects.all()
    dumper(companies)
    dumper(categories)
    return render(request, template, {
        'companies': companies,
        'categories': categories
    })

def company_detail_view(request, company_id):
    template = 'company/detail.html'
    company = Company.objects.get(id=company_id)
    categories = Category.objects.filter(company_id=company_id)
    
    cart = Cart(request.session)
    items = cart.items
    return render(request, template, {
        'company': company,
        'categories': categories,
        'products_in_cart': items
    })