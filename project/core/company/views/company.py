from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import render

from ..forms.company import CompanyForm
from ..models import Company


def company_list_view(request):
    companies = Company.objects.all()
    template = 'company/list.html'

    return render(request, template, {'companies': companies})