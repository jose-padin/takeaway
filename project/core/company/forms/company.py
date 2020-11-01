from django import forms
# from address.models import AddressField


class CompanyForm(forms.Form):
    name = forms.CharField(max_length=150, label='Company name')
    # address = AddressField()
