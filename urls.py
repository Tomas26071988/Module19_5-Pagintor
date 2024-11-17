from django.urls import path
from . import views
from django.views.generic import RedirectView
from .views import sign_up_by_django, sign_up_by_html

urlpatterns = [
    path('', RedirectView.as_view(url='django_sign_up/', permanent=False), name='redirect_sign_up'),
    path('django_sign_up/', sign_up_by_html, name='sign_up_html'),
    path('sign_up/', sign_up_by_django, name='sign_up_django'),
    path('home', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('cart/', views.cart, name='cart'),
]
