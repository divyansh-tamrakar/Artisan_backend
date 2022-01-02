from django import forms
from .models import UserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):

    class Meta:
        model = UserForm
        fields = ['username', 'password', 'password2', 'email']





