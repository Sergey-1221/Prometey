from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    # Include your custom fields here
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields # + ('vkontakte',)
