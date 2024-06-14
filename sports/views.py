from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from sports.models import Product
from django.contrib.auth.views import LoginView
from .forms import LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
# def home(request):
#     return HttpResponse("<strong>Hello World")


def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'sports/index.html', context)


def detail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {'product': product}
    return render(request, 'sports/detail.html', context)


# sports/views.py

# my_projects/sports/views.py


@login_required
def home(request):
    return render(request, 'sports/home.html')
