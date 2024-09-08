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

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        return context
    
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:

        try:
            cart_item = CartItem.objects.filter(user=request.user)
            products = cart_item[0].products.all()

            context = {'items': products}

            return render(request, template_name='cart.html', context=context)
        
        except:
            return HttpResponse("Продуктов в корзине нет")
    

@login_required()
def addProductToCart(request: HttpRequest, product_id):

    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)

        if (product in CartItem.objects.all()[0].products.all()) == False:
            user_cart = CartItem.objects.get(user=request.user)
            user_cart.products.add(product)


    return HttpResponseRedirect('/')


@login_required()
def delProductOfCart(request: HttpRequest, product_id):

    if request.method == 'POST':
        products_from_cart = CartItem.objects.all()[0]
        product = get_object_or_404(Product, id=product_id)

        products_from_cart.products.remove(product)

        return HttpResponseRedirect('/cart/')
    
    else:
        return HttpResponseNotFound()