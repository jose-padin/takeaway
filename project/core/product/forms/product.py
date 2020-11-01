from django import forms

# from core.category.models import Category

from ..models.product import Product


class ProductForm(forms.Form):
    name = forms.CharField(max_length=255)
    description = forms.CharField(max_length=255)
    allergens = forms.CharField(max_length=255)
    price = forms.DecimalField(
        max_digits=8,
        decimal_places=2
    )
    # category = forms.ModelMultipleChoiceField(queryset=Category.objects.all())
    
    # class Meta:
    #     model = Product
    #     fields = ['name', 'description', 'allergens', 'price']