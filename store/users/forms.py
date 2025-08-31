from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from users import User

class Login(AuthenticationForm):
    pass

class Sign(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')