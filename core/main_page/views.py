from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Product, CartItem
from main_page.forms import SearchForm

# Create your views here.


class MainPage(TemplateView):
    template_name = 'main_page.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context['products'] = Product.objects.all()
        context['search'] = SearchForm

        return context
    
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:

        try:
            active_user = request.user
            user_cart = CartItem.objects.get(user=active_user)
            count_products = len(user_cart.products.all())

            context = {
                'count_products': count_products,
                'products': Product.objects.all(),
                'search': SearchForm
            }

            return render(request=request, template_name='main_page.html', context=context)

        except:
            pass

        return super().get(request, *args, **kwargs)
    
    def post(self, request: HttpRequest):

        search = request.POST['search']

        product = Product.objects.filter(title=search)

        context = {
            "products": product,
            "search": SearchForm(request.POST)
        }

        return render(request, 'main_page.html', context)