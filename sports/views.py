from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from sports.models import Product


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
