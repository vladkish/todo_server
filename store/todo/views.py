from django.shortcuts import render, redirect
from .forms import FormCategory, FormTask
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'todo/task.html')

@login_required
def form_task(request):
    
    if request.method == 'POST':
        if request.POST.get("form_type") == 'task':
            task_form = FormTask(data=request.POST)
            category_form = FormCategory()
            if task_form.is_valid():
                task = task_form.save(commit=False)
                task.user = request.user
                task.save()
                return redirect(request.META['HTTP_REFERER'])
        else:
            category_form = FormCategory(data=request.POST)
            task_form = FormTask()
            if category_form.is_valid():
                task = category_form.save(commit=False)
                task.user = request.user
                task.save()
                return redirect(request.META['HTTP_REFERER'])
    else:
        task_form = FormTask()
        category_form = FormCategory()
        
    context = {
        'task_form' : task_form,
        'category_form' : category_form
    }
    
    return render(request, 'todo/create_task.html', context)