import sys

from pprint import PrettyPrinter

from django import forms
from django.contrib.auth.hashers import make_password

from ..models import BaseUser, AdminUser


dumper = PrettyPrinter(indent=4, stream=sys.stderr).pprint


class RegisterForm(forms.Form):
    name = forms.CharField(max_length=120)
    password = forms.CharField(
        max_length=120,
        widget=forms.PasswordInput()
    )
    email = forms.EmailField(max_length=120)
    phone_number = forms.IntegerField()

    def clean(self):
        try:
            user = BaseUser.objects.get(email=self.data['email'])
        except:
            user = None

        if user:
            raise forms.ValidationError('Ya exsite un usuario con ese email')
        
    def save(self):
        AdminUser.objects.create(
            name=self.data['name'],
            password=make_password(self.data['password']),
            email=self.data['email'],
            phone_number=self.data['phone_number'],
            type='Admin'
        )