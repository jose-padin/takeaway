import sys

from pprint import PrettyPrinter

from django import forms
from django.core.mail import send_mail
from django.template import loader

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
        max_length='200',
        label='Nombre del restaurante'    
    )
    postal_code = forms.IntegerField(
        label='Código Postal',
        min_value=1000,
        max_value=52080,
        error_messages={
            'invalid': 'El código postal no existe',
        }
    )
    mobile_phone = forms.IntegerField(
        label='Móvil',
        required=False,
        min_value=1
    )
    email = forms.EmailField(
        label='Email',
    )