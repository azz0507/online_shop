from sports.models import Product
# from django.contrib.auth.views import LoginView
# from .forms import LoginForm
# from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login


# Create your views here.
# def home(request):
#     return HttpResponse("<strong>Hello World")

def index(request):
    products = Product.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("index")

    context = {'products': products}
    return render(request, 'sports/index.html', context)


def detail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {'product': product}
    return render(request, 'sports/detail.html', context)

# sports/views.py

# my_projects/sports/views.py


# @login_required
# def home(request):
#     return render(request, 'sports/login.html')
