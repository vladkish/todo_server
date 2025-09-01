from django import forms
from .models import Category, Task

class FormTask(forms.ModelForm):
    class Meta:
        fields = ('title', 'description', 'category')
        model = Task
        
class FormCategory(forms.ModelForm):
    class Meta:
        fields = ('title', )
        model = Category