from django import forms
from .models import Category, Task

class FormCreateTask(forms.ModelForm):
    class Meta:
        fields = ('title', 'description', 'category')
        model = Task
        
        
class FormCreateCategory(forms.ModelForm):
    class Meta:
        fields = ('title', )
        model = Category