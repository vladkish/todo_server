from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from users.models import User

class Login(AuthenticationForm):
    pass

class Sign(UserCreationForm):

    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')