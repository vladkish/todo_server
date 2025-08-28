from django.db import models
from users.models import User

class Category(models.Model):
    title = models.CharField(max_length=60)
    
    def __str__(self):
        return f'{self.title}'

class Task(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    status = models.BooleanField(default=False)
    date_public = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name='tasks')
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='tasks')
    
    def __str__(self):
        return f'{self.title}, {self.description}, {self.category}'