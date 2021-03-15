import os
from django.conf import settings
from django.views.generic import TemplateView
from django.shortcuts import render

class HomePage(TemplateView):
    template_name = 'index.html'

class AboutPage(TemplateView):
    template_name = 'about.html'

class CovidPage(TemplateView):
    template_name = 'covid.html'