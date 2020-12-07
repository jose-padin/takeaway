import sys

from pprint import PrettyPrinter

from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render

from ..forms.restaurant import RegisterForm, SendEmailForm

from core.company.models import Company
from core.user.models import BaseUser

dumper = PrettyPrinter(indent=4, stream=sys.stderr).pprint


def register(request):
    '''
    This method sends an email to an restaurant admin to 
    register in app
    '''
    template = 'restaurant/register.html'

    if request.method == 'POST':
        form = SendEmailForm(request.POST)

        if form.is_valid():
            form.send_email()
            return redirect('restaurant:form_sent')
    else:
        form = SendEmailForm

    return render(request, template, {'form': form})

def add(request):
    template = 'restaurant/add.html'
    user_email = request.user
    try:
        user = BaseUser.objects.get(email=user_email)
    except BaseUser.DoesNotExist:
        raise HttpResponseForbidden()
        
    # check if user already has a company
    try:
        company = Company.objects.get(admin=user)
    except Company.DoesNotExist:
        company = None

    # if user has company, redirect him/her to add products/categories/etc
    if company:
        return redirect('company:list')

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid(user):
            return redirect('company:list')

    else:
        form = RegisterForm

    return render(request, template, {'form': form})

def form_sent(request, *args, **kwargs):
    template = 'restaurant/form_sent.html'
    return render(request, template)
