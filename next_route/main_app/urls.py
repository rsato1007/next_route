from django.urls import path
from . import views

urlpatterns = [
    # main URLs
    # List of routes I need: search page, splash
    path('', views.Splash.as_view(), name="splash_page"),
    path('accounts/signup/', views.Signup.as_view(), name='signup')

    # route urls
    # List of routes I need: create, edit, delete, view

    # user urls
    # List of users I need: profile page, create user, edit user, delete user (icebox)

    # review urls
    # Add, edit, delete

    # like urls
    # add, delete
]