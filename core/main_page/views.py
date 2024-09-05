from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.base import ContextMixin

# Create your views here.


class MainPage(TemplateView, ContextMixin):
    template_name = 'main_page.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        return context