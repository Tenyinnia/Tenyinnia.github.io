from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, TemplateView, FormView

class LandingPageView(TemplateView):
    template_name = 'index.html'