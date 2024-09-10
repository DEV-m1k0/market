from typing import Any
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpRequest, HttpResponse
from .forms import RegistrationForm
from django.contrib import messages

# Create your views here.


class RegUser(TemplateView):
    template_name = 'reg.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context['reg_form'] = RegistrationForm()

        return context

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:

        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            messages.success(request, "You have signed up successfully")
            return redirect('login')
        
        else:
            return render(request, 'reg.html', context={'reg_form': form})