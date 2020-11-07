from django.shortcuts import render
# from django.views.generic import ListView
from django.shortcuts import render

from core.product.models import Product, Category, ProductCategory
from core.cart.cart import Cart

from ..forms.company import CompanyForm
from ..models import Company

def company_list_view(request):
    template = 'company/list.html'
    companies = Company.objects.all()

    return render(request, template, {'companies': companies})

def company_detail_view(request, company_id):
    template = 'company/detail.html'
    company = Company.objects.get(id=company_id)
    categories = Category.objects.filter(company_id=company_id)
    
    cart = Cart(request.session)
    return render(request, template, {
        'company': company,
        'categories': categories,
    })