from django.contrib.auth.forms import AdminUserCreationForm, UserChangeForm

from .models import LockinUser

class LockinUserCreationForm(AdminUserCreationForm):

    class Meta:
        model = LockinUser
        fields = ("email", "password")

class LockinUserChangeForm(UserChangeForm):

    class Meta:
        model = LockinUser
        fields = ("email", "password")