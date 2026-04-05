from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import LockinUserCreationForm, LockinUserChangeForm
from .models import LockinUser, LockinActivity, LockinActivityNotes
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

class LockinActivityAdmin(admin.ModelAdmin):
    model = LockinActivity
    list_display = [
        'activity_username',
        'activity_name',
        'activity_description'
    ]

class LockinActivityNotesAdmin(admin.ModelAdmin):
    model = LockinActivityNotes
    list_display = [
        'note_text',
    ]

admin.site.register(LockinUser, LockinUserAdmin)
admin.site.register(LockinActivityNotes, LockinActivityNotesAdmin)
admin.site.register(LockinActivity, LockinActivityAdmin)