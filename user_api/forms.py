from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import AppUser

class CustomUserCreationForm(UserCreationForm):
  class Meta:
    model = AppUser
    fields = ('email',)

class CustomUserChangeForm(UserChangeForm):
  class Meta:
    model = AppUser
    fields = UserChangeForm.Meta.fields
