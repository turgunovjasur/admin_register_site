from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic


def login_required_decorator(func):
    return login_required(func, login_url='login_page')


@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect('login_page')


def login_page(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, password=password, username=username)
        if user is not None:
            login(request, user)
            return redirect('home_page')

    return render(request, 'login_html')


@login_required_decorator
def home_page(request):
    return render(request, 'index.html')


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login_page')
    tamplate_name = 'signup.html'
