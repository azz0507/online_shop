from django.conf import settings
from django.conf.urls.static import static
from sports.views import index
from django.urls import path
from django.contrib.auth import views as auth_views
from sports import views

# my_projects/sports/urls.py


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='sports/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.index, name='index'),  # ваша домашняя страница
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
