from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.form_task, name="create_task")
]