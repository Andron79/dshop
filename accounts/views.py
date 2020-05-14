from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from dshop.models import Category
from .forms import SignUpEmailForm


def signup(request):
    categories = Category.objects.all()
    template = 'accounts/signup.html'
    if request.method == 'POST':
        form = SignUpEmailForm(request.POST)
        if form.is_valid():
            form.save()
        username = form.cleaned_data.get('username')
        my_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=my_password)
        login(request, user)
        return redirect('dshop:index')
    else:
        form = SignUpEmailForm()
        return render(request, template, {'form': form,
                                          'categories': categories})
