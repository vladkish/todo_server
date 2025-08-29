from django.shortcuts import render, redirect
from .forms import FormCreateTask, FormCreateCategory
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'todo/task.html')

@login_required
def form_task(request):
    
    if request.method == 'POST':
        if 'task' in request.POST:
            task_form = FormCreateTask(request.POST)
            category_form = FormCreateCategory()
            if task_form.is_valid():
                task = task_form.save(commit=False)
                task.user = request.user
                task.save()
                return redirect(request.META['HTTP_REFERER'])

        else:
            category_form = FormCreateCategory(request.POST)
            task_form = FormCreateTask()
            if category_form.is_valid():
                task = category_form.save(commit=False)
                task.user = request.user
                task.save()
                return redirect(request.META['HTTP_REFERER'])
    else:
        task_form = FormCreateTask()
        category_form = FormCreateCategory()
        
    context = {
        'task_form' : task_form,
        'category_form' : category_form
    }
    
    return render(request, 'todo/create_task.html', context)