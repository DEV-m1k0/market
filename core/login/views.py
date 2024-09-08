from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
# Create your views here.

class LoginView(LoginView):
    template_name = 'login.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context['form'] = AuthenticationForm

        return context