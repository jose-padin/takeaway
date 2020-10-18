from django import forms

from ..models.cart import Cart

class CartForm(forms.ModelForm):

    class Meta:
        model = Cart
        # fields = []