from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import users
from django.contrib.auth.forms import AuthenticationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    date_of_birth = forms.DateField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'date_of_birth']

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)
