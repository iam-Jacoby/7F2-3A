from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm

from django.contrib.auth.decorators import login_required

@login_required(login_url="login/")
def defaultView(request):
    return redirect('home')

def logoutView(request):
    logout(request)
    return redirect('login')

def loginView(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.add_message(request, messages.ERROR, "Invalid username or password")
    else:
        form = UserLoginForm()
    
    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


def home(request):
    if request.user.is_authenticated:
        user_info = {
            'username': request.user.username,
            'email': request.user.email,
        }
        return render(request, 'home.html', {'user_info': user_info})
    else:
        return HttpResponse("You are not logged in.")