from pprint import PrettyPrinter

from django.shortcuts import render
# from django.views.generic import ListView
from django.shortcuts import render

from core.product.models import Product, Category, ProductCategory

from ..forms.company import CompanyForm
from ..models import Company


dumper = PrettyPrinter(indent=4).pprint

def company_list_view(request):
    template = 'company/list.html'
    companies = Company.objects.all()

    return render(request, template, {'companies': companies})

def company_detail_view(request, id):
    template = 'company/detail.html'
    company = Company.objects.get(id=id)
    categories = Category.objects.filter(company_id=id)
    print(categories)

    return render(request, template, {
        'company': company,
        'categories': categories,
    })