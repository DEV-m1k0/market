from typing import Any
from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import ContextMixin
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from main_page.models import Product, CartItem
from django.contrib.auth.models import User

# Create your views here.

class CartView(LoginRequiredMixin, TemplateView):
    template_name = 'cart.html'
    login_url = '/user/login/'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        return context
    
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:

        try:
            cart_item = CartItem.objects.filter(user=request.user)
            print(cart_item)
            products = cart_item[0].products.all()

            context = {'items': products}

            return render(request, template_name='cart.html', context=context)
        
        except:
            return HttpResponse("Продуктов в корзине нет")
    

def addProductToCart(request: HttpRequest, product_id):

    if request.method == 'POST':
        # cart = get_object_or_404(Cart, user=request.user)
        product = get_object_or_404(Product, id=product_id)

        if (product in CartItem.objects.all()[0].products.all()) == False:
            user_cart = CartItem.objects.get(user=request.user)
            user_cart.products.add(product)

        # try:
        #     print('start')
        #     cart_items = CartItem.objects.filter(cart=cart, products=product)
        #     print(cart_items)
            
        #     if len(cart_items) == 0:
        #         new_item = CartItem.objects.create(cart=cart, products=product)
        #         new_item.save()

        # except:
        #     pass


    return HttpResponseRedirect('/')