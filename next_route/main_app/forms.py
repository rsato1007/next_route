from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class MyUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'location', 'is_admin', 'is_banned')

class MyUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('username', 'location', 'is_admin', 'is_banned')

class UpdateProfile(forms.ModelForm):
    username = forms.CharField(required=True)
    email = forms.CharField(required=True)
    password = forms.CharField(required=True)
    location = forms.CharField(required=True)
    url = forms.CharField(required=False)

    class Meta:
        model = CustomUser
        fields = ("username", "email", "password", "location", "url")