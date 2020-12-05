import sys

from pprint import PrettyPrinter

from django.shortcuts import redirect, render

from ..forms.restaurant import SendEmailForm

dumper = PrettyPrinter(indent=4, stream=sys.stderr).pprint


def register(request):
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
    return render(request, template)

def form_sent(request, *args, **kwargs):

    template = 'restaurant/form_sent.html'
    return render(request, template)