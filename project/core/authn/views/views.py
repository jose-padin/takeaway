import sys

from pprint import PrettyPrinter

from django import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

dumper = PrettyPrinter(indent=4, stream=sys.stderr).pprint


class LoginForm(AuthenticationForm):
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(username=username,
                                           password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login',
                    params={'username': self.username_field.verbose_name},
                )
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

def login_user(request):
    template = 'authn/login.html'
    form = LoginForm()

    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        email = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('company:list')
        else:
            # Return an 'invalid login' error message.
            messages.error(request,'username or password not correct')
            return render(request, template, {'form': form})
    
    return render(request, template, {'form': form})
    

def logout_user(request):
    logout(request)
