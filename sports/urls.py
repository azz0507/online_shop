from django.urls import path
from sports.views import index

urlpatterns = [
    path('', index, name='index')

]

