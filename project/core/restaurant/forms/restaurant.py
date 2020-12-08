import sys

from pprint import PrettyPrinter

from django import forms
from django.core.mail import send_mail
from django.template import loader

from core.company.models import Company

dumper = PrettyPrinter(indent=4, stream=sys.stderr).pprint


class SendEmailForm(forms.Form):
    name = forms.CharField(
        max_length='200',
        label='Nombre del restaurante'    
    )
    email = forms.EmailField(
        label='Email',
    )
        
    def send_email(self):
        template = loader.get_template('restaurant/email.html')
        url = 'http://localhost:9988/user/add'
        
        html_message = template.render({
            'url': url
        })
         
        send_mail(
            'Registro',
            None,
            None,
            [self.cleaned_data['email']],
            fail_silently=False,
            html_message=html_message
        )

class RegisterForm(forms.Form):
    name = forms.CharField(
        label='Nombre del restaurante',
        max_length='200',
    )
    address = forms.CharField(
        label='Dirección',
        max_length=255,
    )
    postal_code = forms.IntegerField(
        label='Código Postal',
        min_value=1000,
        max_value=52080,
        error_messages={
            'invalid': 'El código postal no existe',
        }
    )
    description = forms.CharField(
        label='Descripción',
        max_length=255,
        required=True
    )
    image = forms.ImageField(
        label='Imagen principal',
        required=False
    )
    logo = forms.ImageField(
        label='Logo',
        required=False
    )
    
    def is_valid(self, user):
        Company.objects.create(
            name=self.data['name'],
            address=self.data['address'],
            postal_code=self.data['postal_code'],
            description=self.data['description'],
            image=self.data['image'],
            logo=self.data['logo'],
            admin=user
        )
        return self.data


