import sys

from pprint import PrettyPrinter

from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView

from core.user.models import AdminUser

from ..forms.product import ProductForm, ProductUpdateForm
from ..models.product import Product, ProductCategory, Category

dumper = PrettyPrinter(indent=4, stream=sys.stderr).pprint

TEMPLATE = 'product'


# class ProductListView(ListView):
#     model = Product

#     def get(self, request, *args, **kwargs):
#         products = Product.objects.filter(is_deleted=False)
#         return render(request, f'{TEMPLATE}/list.html', {'products': products})


def list_by_category(request, category_id):
    template = 'product/list_by_category.html'
    category = Category.objects.get(id=category_id)
    products = category.products.filter(is_deleted=False)
    return render(request, template, {
        'products': products,
        'category': category    
    })


def add(request, category_id):
    template = f'{TEMPLATE}/add.html'
    form = ProductForm()

    if request.method == 'POST':
        user = AdminUser.objects.get(email=request.user.email)
        form = ProductForm(request.POST)

        if form.is_valid(user, category_id):
            return redirect('product:list_by_category', category_id)
        else:
            messages.error(request, 'Ese producto ya existe')

    return render(request, template, {'form': form})


def edit(request, product_id):
    template = 'product/update.html'
    context = {}
    product = get_object_or_404(Product, id=product_id)
    form = ProductUpdateForm(request.POST or None, instance=product)

    if form.is_valid():
        form.save()
        return redirect('restaurant:list_categories')
    
    context['form'] = form
    return render(request, template, context)


def delete(request, product_id):
    product = Product.objects.get(id=product_id)
    product.is_deleted = True
    product.save()
    return redirect('restaurant:list_categories')