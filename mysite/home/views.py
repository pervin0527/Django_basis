from django.shortcuts import render
from django.views.generic import TemplateView, ListView

# Create your views here.

class HomeView(TemplateView):
    """
    Home Page View
    """
    template_name = 'home/home.html'