from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class User(AbstractUser):
    image = models.ImageField(upload_to='users/')