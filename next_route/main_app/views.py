from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
# This is only temporary until I actually add something.
from django.http import HttpResponse

# Create your views here.
class Splash(TemplateView):
    template_name = "splash.html"