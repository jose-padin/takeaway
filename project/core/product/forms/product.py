import sys

from pprint import PrettyPrinter

from django import forms

from core.company.models import Company
from core.product.models import Category

from ..models.product import Product

dumper = PrettyPrinter(indent=4, stream=sys.stderr).pprint


class ProductForm(forms.Form):
    name = forms.CharField(
        label='Nombre',
        max_length=255
    )
    description = forms.CharField(
        label='Descripción',
        max_length=255
    )
    allergens = forms.CharField(
        label='Alérgenos',
        required=False,
        max_length=255
    )
    price = forms.DecimalField(
        label='Precio',
        max_digits=8,
        decimal_places=2
    )

    def is_valid(self, user, category_id):
        company = Company.objects.get(admin=user)
        category = Category.objects.get(id=category_id)

        try:
            product = Product.objects.get(name=self.data['name'])
        except Product.DoesNotExist:
            product = None

        if product:
            return False

        product = Product.objects.create(
            name=self.data['name'],
            description=self.data['description'],
            allergens=self.data['allergens'],
            price=self.data['price'],
            company=company
        )

        category.products.add(product)
        
        return super().is_valid()
        

class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'allergens', 'price']


class CategoryForm(forms.Form):
    name = forms.CharField(
        label='Nombre',
        max_length=120
    )

    def is_valid(self, company):
        self.company = company
        category_name = self.data['name']
        try:
            category = Category.objects.get(
                name=category_name,
                company=self.company
            )
        except Category.DoesNotExist:
            category = None
        
        if category:
            return False

        Category.objects.create(
            name=self.data['name'],
            company=company
        )
        
        return super().is_valid()


class CategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']