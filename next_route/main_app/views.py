from django.shortcuts import render, redirect, reverse
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from .models import Route, CustomUser, Review, Like
from .forms import MyUserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# This is only temporary until I actually add something.
from django.http import HttpResponse

# Create your views here.
class Splash(TemplateView):
    template_name = "splash.html"

# Account Related Views
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

class ProfilePage(TemplateView):
    model = CustomUser
    template_name = 'profile.html'
    # What does this do: ordering = ['created_at']

    def get_context_data(self, pk, **kwargs):
        user = CustomUser.objects.get(pk=pk)
        context = super().get_context_data(**kwargs)
        context["user_profile"] = user
        # This will be our template for when the user starts posting routes and reviews.
        context["routes"] = user.route.all().order_by('-created_at')
        context["reviews"] = user.review.all().order_by('-posted_at')
        return context

# @method_decorator(login_required, name='dispatch')
# Add this to the create route view and review route.