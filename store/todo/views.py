from django.shortcuts import render

def index(request):
    return render(request, 'todo/task.html')

def form_task(request):
    return render(request, 'todo/create_task.html')