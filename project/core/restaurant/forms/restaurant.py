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
    postal_code = forms.IntegerField(
        label='Código Postal'
    )
    mobile_phone = forms.IntegerField(
        label='Móvil'
    )
    email = forms.EmailField(
        label='Email'
    )

    def send_email(self):
        template = loader.get_template('restaurant/email.html')
        url = 'http://localhost:9988/restaurant/add'
        
        html_message = template.render({
            'url': url
        })
         
        send_mail(
            'Registro',
            None,
            'mendezpadin.jose@gmail.com',
            [self.cleaned_data['email']],
            fail_silently=False,
            html_message=html_message
        )