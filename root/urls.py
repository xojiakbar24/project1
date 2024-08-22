from root import settings
from django.conf.urls.static import static
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

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

