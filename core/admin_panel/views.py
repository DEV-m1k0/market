from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class AdminPanelView(TemplateView):
    template_name = 'admin_panel.html'
