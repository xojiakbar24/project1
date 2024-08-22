"""
URL configuration for root project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps.views import (IndexView, ShopView, AboutView, ServiceView, BlogView,
                        ContactView, CartView, PaymentView, ThanksView, SignUpView,add_to_cart)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('about', AboutView.as_view(), name='about'),
    path('service', ServiceView.as_view(), name='service'),
    path('blog', BlogView.as_view(), name='blog'),
    path('contact', ContactView.as_view(), name='contact'),
    path('cart', CartView.as_view() ,name='cart'),
    path('checkout', PaymentView.as_view(),name='checkout'),
    path('thanks', ThanksView.as_view(),name='thanks'),
    path('signup',SignUpView.as_view(),name='signup'),
    #  path('add-to-cart/<int:pk>/', add_to_cart, name='add_to_cart'),
]

