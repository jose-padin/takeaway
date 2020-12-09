import sys

from pprint import PrettyPrinter

from django import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from ..forms.forms import LoginForm

dumper = PrettyPrinter(indent=4, stream=sys.stderr).pprint


def login_user(request):
    template = 'authn/login.html'
    form = LoginForm()

    if request.user.is_authenticated:
        return redirect('company:list')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        email = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('company:list')
        else:
            # Return an 'invalid login' error message.
            messages.error(
                request,
                'El nombre de usuario o la contraseña son incorrectos.'
            )
            return render(request, template, {'form': form})
    
    return render(request, template, {'form': form})
    

def logout_user(request):
    cart = request.session
    cart.clear()
    logout(request)

    return redirect('/')
