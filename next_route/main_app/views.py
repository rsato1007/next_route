from django.shortcuts import render
from django.views import View
# This is only temporary until I actually add something.
from django.http import HttpResponse

# Create your views here.
class Splash(View):

    def get(self, request):
        return HttpResponse("This is your sanity check buddy")