from typing import Any
import PIL.Image
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.base import ContextMixin
from .models import Product
from PIL import Image

# Create your views here.


class MainPage(TemplateView, ContextMixin):
    template_name = 'main_page.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context['products'] = Product.objects.all()

        return context
    
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().get(request, *args, **kwargs)