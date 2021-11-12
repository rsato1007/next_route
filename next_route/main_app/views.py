from django.shortcuts import render, redirect, reverse
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from .models import Route, CustomUser, Review, Like
from .forms import MyUserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# This is only temporary until I actually add something.
from django.http import HttpResponse
from django.db.models import Q
from decimal import Decimal
import operator
from functools import reduce

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

# When you do search, use this as part of the search algorithm: https://stackoverflow.com/questions/33104897/django-filter-objects-by-integer-between-two-values

# Route Related Views
# Function that returns a list of pitch ranges based on user input.
def pitch_range(max_val):
    max = int(max_val)
    if max >= 10:
        max = 10
    range_value = []
    for i in range(0, max + 1):
        range_value.append(i)
    return range_value

# Crafting function that returns a list of difficulty values:
def difficulty_range(val1, val2):
    # Validation 1
    if type(val1) != type("string"):
        print("error")
    val1 = val1.split(".")
    val2 = val2.split(".")
    min = int(val1[1])
    max = int(val2[1])
    # Validation 2
    if max < min:
        print("Error")
    # Validation 3
    elif max > 15 or int(val1[0]) <= 4:
        print("Error")
    value_range = []
    if min < 10 and max >= 10:
        for i in range(min, 10):
            num = "5." + str(i)
            value_range.append(num)
        for i in range(10, max + 1):
            num = "5." + str(i) + "a"
            value_range.append(num)
            num = "5." + str(i) + "b"
            value_range.append(num)
            num = "5." + str(i) + "c"
            value_range.append(num)
            num = "5." + str(i) + "d"
            value_range.append(num)
    elif min < 10 and max < 10:
        for i in range(min, max + 1):
            num = "5." + str(i)
            value_range.append(num)
    else:
        for i in range(min, max + 1):
            num = "5." + str(i) + "a"
            value_range.append(num)
            num = "5." + str(i) + "b"
            value_range.append(num)
            num = "5." + str(i) + "c"
            value_range.append(num)
            num = "5." + str(i) + "d"
            value_range.append(num)
    return value_range

class RouteSearch(ListView):
    template_name="search.html"

    # This code is temporary.
    def get_queryset(self):
        # This allows me to go to this page even if no query is being made.
        if not self.request.GET:
            print("ROUTE SEARCH")
        else:
            # Good Problem: We're providing two values and we only want a list returned with values in between those two.
            # Let's do Validations in here instead.
            min_difficulty = self.request.GET.get("min-difficulty")
            max_difficulty = self.request.GET.get('max-difficulty')
            q = difficulty_range(min_difficulty, max_difficulty)
            return Route.objects.filter(
                difficulty__in=q,
                pitch__range=(0, int(self.request.GET.get("max-pitches"))),
                location__icontains=self.request.GET.get("location")
            )

class CreateRoute(View):

    def get(self, request):
        return render(request, 'create_route.html')

    def post(self, request):
        name = request.POST.get('name')
        location = request.POST.get('location')
        difficulty = request.POST.get('difficulty')
        description = request.POST.get('description')
        image = request.POST.get('image')
        climb_type = request.POST.get('climb_type')
        pitch = request.POST.get('pitch')
        user = CustomUser.objects.get(pk=request.POST.get('user'))
        Route.objects.create(name=name, location=location, difficulty=difficulty, description=description, image=image, climb_type=climb_type, pitch=pitch, user=user)
        return redirect('route_search')