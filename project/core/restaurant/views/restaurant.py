import sys

from pprint import PrettyPrinter

from django.contrib import messages
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render

from ..forms.restaurant import (
    RegisterForm,
    SendEmailForm
)

from core.company.models import Company
from core.product.forms.product import CategoryForm, CategoryUpdateForm
from core.product.models import Category
from core.user.models import AdminUser

dumper = PrettyPrinter(indent=4, stream=sys.stderr).pprint


def register(request):
    '''
    This method sends an email to register a restaurant admin in app
    '''
    template = 'restaurant/register.html'

    if request.method == 'POST':
        form = SendEmailForm(request.POST)

        if form.is_valid():
            form.send_email()
            return redirect('restaurant:form_sent')
    else:
        form = SendEmailForm

    return render(request, template, {'form': form})


def add(request):
    template = 'restaurant/add.html'
    user_email = request.user
    try:
        user = AdminUser.objects.get(email=user_email)
    except AdminUser.DoesNotExist:
        raise HttpResponseForbidden()
        
    # check if user already has a company
    try:
        company = Company.objects.get(admin=user)
    except Company.DoesNotExist:
        company = None

    # if user has company, redirect him/her to list_categories
    if company:
        return redirect('restaurant:list_categories')

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid(user):
            return redirect('company:list')

    else:
        form = RegisterForm

    return render(request, template, {'form': form})


def add_category(request):
    template = 'restaurant/add_category.html'
    form = CategoryForm
    company = Company.objects.get(admin=request.user)

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid(company):
            return redirect('restaurant:list_categories')
        else:
            messages.error(request, 'Esa categoría ya existe')

    return render(request, template, {
        'form': form, 
        'company': company
        }
    )


def list_categories(request):
    template = 'restaurant/list_categories.html'
    company = Company.objects.get(admin=request.user)
    categories = Category.objects.filter(
        company=company,
        is_deleted=False
    )
    return render(request, template, {
        'categories': categories
    })


def edit_category(request, category_id):
    template = 'restaurant/update_category.html'
    context = {}
    category = get_object_or_404(Category, id=category_id)
    form = CategoryUpdateForm(request.POST or None, instance=category)

    if form.is_valid():
        form.save()
        return redirect('restaurant:list_categories')
    
    context['form'] = form
    return render(request, template, context)


def delete_category(request, category_id):
    category = Category.objects.get(id=category_id)
    category.is_deleted = True
    category.save()
    return redirect('restaurant:list_categories')


def form_sent(request, *args, **kwargs):
    template = 'restaurant/form_sent.html'
    return render(request, template)
