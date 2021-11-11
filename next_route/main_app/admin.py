from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import MyUserCreationForm, MyUserChangeForm
from .models import CustomUser, Route, Review, Like

# Register your models here.
class MyUserAdmin(UserAdmin):
    add_form = MyUserCreationForm
    form = MyUserChangeForm
    model = CustomUser
    list_display = ['username', 'location', 'is_admin', 'is_banned']
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('location', 'is_admin', 'is_banned')}),
    ) #this will allow to change these fields in admin module


admin.site.register(CustomUser, MyUserAdmin)
admin.site.register(Route)
admin.site.register(Review)
admin.site.register(Like)