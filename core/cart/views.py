from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from main_page.models import Product, CartItem
from django.contrib.auth.decorators import login_required


# Create your views here.

class CartView(LoginRequiredMixin, TemplateView):
    template_name = 'cart.html'
    login_url = '/user/login/'
    
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:

        try:
            cart_item = CartItem.objects.filter(user=request.user)
            products = cart_item[0].products.all()

            context = {'items': products}

            return render(request, template_name='cart.html', context=context)
        
        except:
            return render(request, template_name='cart.html')
    

@login_required()
def addProductToCart(request: HttpRequest, product_id):

    if request.method == 'POST':

        product = get_object_or_404(Product, id=product_id)

        print()

        try:
            user_cart = CartItem.objects.get(user=request.user)
            user_cart.products.add(product)

        except:
            cart = CartItem.objects.create(user=request.user)
            cart.products.add(product)
            

    return HttpResponseRedirect('/')


@login_required()
def delProductOfCart(request: HttpRequest, product_id):

    if request.method == 'POST':
        products_from_cart = CartItem.objects.get(user=request.user)
        product = get_object_or_404(Product, id=product_id)
        products_from_cart.products.remove(product)

        return HttpResponseRedirect('/cart/')
    
    else:
        return HttpResponseNotFound()