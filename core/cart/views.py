from typing import Any
from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import ContextMixin
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from main_page.models import Product, Cart, CartItem

# Create your views here.

class CartView(LoginRequiredMixin, View, ContextMixin):
    template_name = 'cart.html'
    login_url = '/user/login/'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        return context
    
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:

        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item = CartItem.objects.filter(cart=cart)
        products = cart_item[0].products.all()

        context = {'items': products}

        return render(request, template_name='cart.html', context=context)