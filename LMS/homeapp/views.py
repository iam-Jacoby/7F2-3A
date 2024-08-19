from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, SignInForm

def home_view(request):
    context = {}
    if request.user.is_authenticated:  # Check if the user is logged in
        context['username'] = request.user.username  # Pass the username to the context

    return render(request, 'homeapp/homepage.html', context)

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')  # Redirect to a home page or any other page
    else:
        form = SignUpForm()
    return render(request, 'homeapp/signup.html', {'form': form})

def signin_view(request):
    if request.method == 'POST':
        form = SignInForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to a home page or any other page
    else:
        form = SignInForm()
    return render(request, 'homeapp/signin.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('signin')
