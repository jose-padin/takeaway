import sys

from pprint import PrettyPrinter

from django import forms
from django.contrib.auth.hashers import make_password

from ..models import BaseUser, AdminUser

dumper = PrettyPrinter(indent=4, stream=sys.stderr).pprint


class RegisterForm(forms.ModelForm):
    class Meta:
        model = AdminUser
        fields = ['first_name', 'last_name', 'password', 'email', 'phone_number']

    def save(self):
        AdminUser.objects.create(
            first_name=self.data['first_name'],
            last_name=self.data['last_name'],
            password=make_password(self.data['password']),
            email=self.data['email'],
            phone_number=self.data['phone_number'],
            type='Admin'
        )