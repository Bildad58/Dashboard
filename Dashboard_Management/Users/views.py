# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from Users.forms import UserRegistrationForm
from django.contrib import messages
from Users.forms import *
from django.contrib.auth import get_user_model

User = get_user_model()

def register(request):
    if request.user.is_authenticated:
        messages.info(request, "You are already logged in.")
        return redirect('dashboard')
        
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Welcome! Your registration was successful.")  # Success message
            return redirect('dashboard')
        else:
            # Get specific form errors
            if 'email' in form.errors:
                messages.error(request, "Email error: This email may already be registered.")
            if 'password1' in form.errors:
                messages.error(request, "Password error: Please ensure your password meets the requirements.")
            if 'password2' in form.errors:
                messages.error(request, "Password confirmation does not match.")
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserRegistrationForm()
    return render(request, 'Users/register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        messages.info(request, "You are already logged in.")
        return redirect('dashboard')
        
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if not email or not password:
            messages.error(request, "Please fill in all fields.")
            return render(request, 'Users/login.html')
            
        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Successfully logged in!")  # Success message with user email
                return redirect('dashboard')
            else:
                messages.error(request, "Invalid password. Please try again.")
        except User.DoesNotExist:
            messages.error(request, "No account found with this email address.")
        
    return render(request, 'Users/login.html')

@login_required
def logout_view(request):
    if request.user.is_authenticated:
        email = request.user.email  # Store email before logout
        logout(request)
        messages.success(request, f"Goodbye! You have been successfully logged out.")  # Success message
    else:
        messages.info(request, "You were not logged in.")
    return redirect('login')