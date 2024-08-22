from django.shortcuts import render,get_object_or_404, redirect
from django.views.generic import TemplateView, ListView
from httpx import post, get
from .models import Product, Cart, CartItem

API_TOKEN = '7123965331:AAGZH1lPJvBchmB8ffsgtTu1uTdqvWx4Udc'


def send_message(chat_id, message):
    url = f'https://api.telegram.org/bot{7123965331:AAGZH1lPJvBchmB8ffsgtTu1uTdqvWx4Udc}/sendMessage'
    params = {
        'chat_id': chat_id,
        'text': message
    }
    response = get(url, params=params)
    print(response.text, response.status_code)

def index(request):
    return render(request, 'index.html')



class IndexView(TemplateView):
    template_name = 'index.html'
    context_object_name = 'index'


class ShopView(ListView):
    model = Product
    template_name = 'shop.html'
    context_object_name = 'shops'

class AboutView(TemplateView):
    template_name = 'about.html'
    context_object_name = 'about'

class ServiceView(TemplateView):
    template_name = 'services.html'
    context_object_name = 'services'

class BlogView(TemplateView):
    template_name = 'blog.html'
    context_object_name = 'blog'

class ContactView(TemplateView):
    template_name = 'contact.html'
    context_object_name = 'contact'

class CartView(TemplateView):
    template_name = 'cart.html'
    context_object_name = 'cart'

class PaymentView(TemplateView):
    template_name = 'checkout.html'
    context_object_name = 'checkout'

class ThanksView(TemplateView):
    template_name = 'thankyou.html'
    context_object_name = 'thanks'

class SignUpView(TemplateView):
    template_name = 'signup.html'
    context_object_name = 'signup'



def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart_view')



