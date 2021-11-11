from django.shortcuts import render, redirect, reverse
from django.views import View
from django.views.generic.base import TemplateView
from .forms import MyUserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# This is only temporary until I actually add something.
from django.http import HttpResponse

# Create your views here.
class Splash(TemplateView):
    template_name = "splash.html"

class Signup(View):
    def get(self, request):
        form = MyUserCreationForm()
        context = {"form": form}
        return render(request, "new_account.html", context)
    
    def post(self, request):
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("splash_page")
        else:
            context = {"form": form}
            return render(request, "new_account.html", context)

# @method_decorator(login_required, name='dispatch')
# Add this to the create route view and review route.