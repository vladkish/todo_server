from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from .forms import Login, Sign
from todo.models import Task

def login(request):
    
    if request.method == "POST":
        form = Login(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(request, username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect('index')
    else:
        form = Login()
        
    context = {
        'form' : form
    }
    
    return render(request, 'users/login.html', context)

def sign(request):
    
    if request.method == 'POST':
        form = Sign(data=request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return redirect('index')
    else:
        form = Sign()
        
    context = {
        'form' : form
    }
    
    return render(request, 'users/sign.html', context)

@login_required
def profile(request):

    context = {
        'posts' : Task.objects.filter(user=request.user)
    }

    return render(request, 'users/profile.html', context)

@login_required
def logout(request):
    auth.logout(request)
    return redirect('index')