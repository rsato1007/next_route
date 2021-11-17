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
    path('route/<int:pk>/', views.RoutePage.as_view(), name="route_page"),
    path('route/<int:pk>/update/', views.RouteUpdate.as_view(), name="route_update"),

    # user urls
    # List of users I need: profile page, create user, edit user, delete user (icebox)
    path('accounts/signup/', views.Signup.as_view(), name='signup'),
    path('profile/<int:pk>/', views.ProfilePage.as_view(), name="profile"),
    path('accounts/<int:pk>/edit/', views.EditProfile.as_view(), name="edit_profile"),

    # review urls
    # Add, edit, delete
    path('route/<int:pk>/review/new/', views.CreateReview.as_view(), name="create_review"),
    path('route/<int:pk>/review/<int:review_pk>/update/', views.ReviewUpdate.as_view(), name="review_update"),
    path('profile/<int:pk>/review/<int:review_pk>/update/', views.ReviewUpdateProfile.as_view(), name="review_update_profile"),
    path('route/<int:pk>/review/<int:review_pk>/delete/', views.ReviewDelete.as_view(), name="review_delete"),
    path('profile/<int:pk>/review/<int:review_pk>/delete/', views.ReviewDeleteProfile.as_view(), name="review_delete_profile")

    # like urls
    # add, delete
]