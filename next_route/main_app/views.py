from django.shortcuts import render, redirect, reverse
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from .models import Route, CustomUser, Review, Like
from .forms import MyUserCreationForm, UpdateProfile
from django.contrib.auth import login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.exceptions import PermissionDenied
# This is only temporary until I actually add something.
from django.http import HttpResponse
from django.db.models import Q
from decimal import Decimal
import operator
from functools import reduce
import uuid
import boto3

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'nextroute'

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
        updated_request = request.POST.copy()
        updated_request["is_admin"] = False
        updated_request["is_banned"] = False
        form = MyUserCreationForm(updated_request)
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

@method_decorator(login_required, name='dispatch')
class EditProfile(View):
    def post(self, request, pk):
        user = CustomUser.objects.filter(pk=pk)
        updatedUser = {}
        # Verification in the event the user used invalid data:
        if request.POST.get('location'):
            updatedUser['location'] = request.POST.get('location')
        else:
            updatedUser['location'] = user[0].location
        if request.POST.get('password'):
            updatedUser['password'] = make_password(request.POST.get('password'))
        else:
            updatedUser['password'] = user[0].password
        if request.FILES.get('image'):
            user_image = request.FILES.get('image', False)
            # This is what generates the URL for our bucket.
            if user_image:
                s3 = boto3.client('s3')
                key = uuid.uuid4().hex[:6] + user_image.name[user_image.name.rfind('.'):]
                s3.upload_fileobj(user_image, BUCKET, key)
                url = f"{S3_BASE_URL}{BUCKET}/{key}"
                updatedUser['url'] = url
        else:
            updatedUser['url'] = user[0].url

        user.update(location = updatedUser['location'], password = updatedUser['password'], url = updatedUser['url'])
        return redirect('profile', pk=pk)

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
        if self.request.GET:
            # Good Problem: We're providing two values and we only want a list returned with values in between those two.
            # Let's do Validations in here instead.
            min_difficulty = self.request.GET.get("min-difficulty")
            max_difficulty = self.request.GET.get('max-difficulty')
            q = difficulty_range(min_difficulty, max_difficulty)
            routes = Route.objects.filter(
                difficulty__in=q,
                pitch__range=(0, int(self.request.GET.get("max-pitches"))),
                location__icontains=self.request.GET.get("location")
            )
            return routes

    # def get_context_data(self, **kwargs):
    #     if self.request.GET:
    #         min_difficulty = self.request.GET.get("min-difficulty")
    #         max_difficulty = self.request.GET.get('max-difficulty')
    #         q = difficulty_range(min_difficulty, max_difficulty)
    #         routes = Route.objects.filter(
    #             difficulty__in=q,
    #             pitch__range=(0, int(self.request.GET.get("max-pitches"))),
    #             location__icontains=self.request.GET.get("location")
    #         )
    #         context = super().get_context_data(**kwargs)
    #         context["routes"] = routes
            

@method_decorator(login_required, name='dispatch')
class CreateRoute(View):

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'create_route.html')
        else:
            raise PermissionDenied()

    def post(self, request):
        route_image = request.FILES.get('image', False)
        url = False
        # This is what generates the URL for our bucket.
        if route_image:
            s3 = boto3.client('s3')
            key = uuid.uuid4().hex[:6] + route_image.name[route_image.name.rfind('.'):]
            s3.upload_fileobj(route_image, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"

        name = request.POST.get('name')
        location = request.POST.get('location')
        difficulty = request.POST.get('difficulty')
        description = request.POST.get('description')
        image = request.POST.get('image')
        climb_type = request.POST.get('climb_type')
        pitch = request.POST.get('pitch')
        user = CustomUser.objects.get(pk=request.user.pk)
        route = Route.objects.create(name=name, location=location, difficulty=difficulty, description=description, url=url, climb_type=climb_type, pitch=pitch, user=user)
        return redirect('route_page', pk=route.pk)

def reviewAverage(reviews):
    i = 0;
    sum = 0;
    for review in reviews:
        i += 1
        sum += review.rating
    if i == 0:
        return 0
    else:
        return sum/i

class RoutePage(DetailView):
    model = Route
    template_name = 'route_page.html'

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        route = Route.objects.get(pk=pk)
        context = super().get_context_data(**kwargs)
        context["reviews"] = route.review.all().order_by('-posted_at')
        context["review_score"] = reviewAverage(context["reviews"])
        return context

@method_decorator(login_required, name='dispatch')
class RouteUpdate(View):
    # model = Route
    # fields = ['name', 'location','difficulty', 'description', 'image', 'climb_type', 'pitch']
    # template_name = "edit_route.html"
    # def get_success_url(self):
    #     return reverse('route_page', kwargs={'pk': self.object.pk})
    
    def get(self, request, pk):
        context = { "route": Route.objects.get(pk=pk), "range": range(11), "difficulty": difficulty_range("5.0", "5.15") }
        return render(request, "edit_route.html", context)

    def post(self, request, pk):
        name = request.POST.get('name')
        location = request.POST.get('location')
        difficulty = request.POST.get('difficulty')
        description = request.POST.get('description')
        image = request.POST.get('image')
        climb_type = request.POST.get('climb_type')
        pitch = request.POST.get('pitch')
        Route.objects.filter(pk=pk).update(name=name, location=location, difficulty=difficulty, description=description, image=image, climb_type=climb_type, pitch=pitch)
        return redirect('route_page', pk=pk)

# ALL REVIEW VIEWS
@method_decorator(login_required, name='dispatch')
class CreateReview(View):
    def post(self, request, pk):
        user = CustomUser.objects.get(pk=request.user.pk)
        route = Route.objects.get(pk=pk)
        rating = request.POST.get('rating')
        content = request.POST.get('content')
        Review.objects.create(user=user, route=route, rating=rating, content=content)
        return redirect('route_page', pk=pk)

@method_decorator(login_required, name='dispatch')
class ReviewUpdate(View):
    def post(self, request, pk, review_pk):
        rating = request.POST.get('rating')
        content = request.POST.get('content')
        Review.objects.filter(pk=review_pk).update(rating=rating, content=content)
        return redirect('route_page', pk=pk)

@method_decorator(login_required, name='dispatch')
class ReviewDelete(View):
    def get(self, request, pk, review_pk):
        review = Review.objects.get(pk=review_pk)
        review.delete()
        return redirect('route_page', pk=pk)