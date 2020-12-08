from django.shortcuts import redirect, render

from ..forms.user import RegisterForm


def add_admin(request):
    template = 'user/add_admin.html'
    form = RegisterForm

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm

    return render(request, template, {'form': form})