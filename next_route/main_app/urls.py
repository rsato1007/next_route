from django.urls import path
from . import views

urlpatterns = [
    # main URLs
    # List of routes I need: search page, splash
    path('', views.Splash.as_view(), name="splash_page"),

    # route urls
    # List of routes I need: create, edit, delete, view
    path('route/', views.RouteSearch.as_view(), name="route_search"),
    path('route/new/', views.CreateRoute.as_view(), name="create_route"),

    # user urls
    # List of users I need: profile page, create user, edit user, delete user (icebox)
    path('accounts/signup/', views.Signup.as_view(), name='signup'),
    path('profile/<int:pk>/', views.ProfilePage.as_view(), name="profile")

    # review urls
    # Add, edit, delete

    # like urls
    # add, delete
]