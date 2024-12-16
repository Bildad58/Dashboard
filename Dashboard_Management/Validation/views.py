from .forms import CustomUserCreationForm,CustomAuthenticationForm
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .models import *

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Validationlogin.html')
    else :
        form = CustomUserCreationForm()
    return render(request, 'Validation/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None: 
                login(request, user)
                messages.success(request, 'Login successfully completed! ')
                return redirect('')   
            else:
                messages.error(request, 'invalid email or password! ')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'Validation/login.html', {'form': form})

def landing_page(request):
    return  render(request, 'Validation/landing_page.html')