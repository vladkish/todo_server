from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from .forms import Login, Sign

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

def sign(requests):
    
    if requests.method == 'POST':
        form = Sign(data=requests.POST)
        if form.is_valid():
            user = form.save()
            auth.login(requests, user)
            return redirect('index')
    else:
        form = Sign()
        
    context = {
        'form' : form
    }
    
    return render(requests, 'users/sign.html', context)

@login_required
def profile(request):
    return render(request, 'users/profile.html')