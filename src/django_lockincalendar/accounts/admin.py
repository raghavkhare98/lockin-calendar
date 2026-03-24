from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import LockinUserCreationForm, LockinUserChangeForm
from .models import LockinUser
# Register your models here.

class LockinUserAdmin(UserAdmin):
    add_form = LockinUserCreationForm
    form = LockinUserChangeForm
    model = LockinUser
    list_display = [
        "email",
        "is_staff",
        "is_active",
    ]
    ordering = ["email"]

admin.site.register(LockinUser, LockinUserAdmin)