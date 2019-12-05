from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.

from accounts.forms import LoginForm


def user_login(request):
    form_fields = LoginForm(request.POST)

    if request.method == "POST":
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect(reverse('cam_registry_list'))
        else:
            context = {
                'form_fields': form_fields,
                'error_message': "Wrong username or password. Try Again."
            }

    else:
        form_fields = LoginForm()
        context = {
            'form_fields': form_fields,
            'error_message': None
        }

    return render(request, 'accounts/login.html', context)


def user_logout(request):
    logout(request)
    return redirect(reverse('LoginUrl'))
