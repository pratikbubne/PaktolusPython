from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as django_login
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from account.form import UserRegisterForm
from django.contrib import messages

# Create your views here.
from account.models import User


def create_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Account has been created!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'create_user.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                    django_login(request, user)
                    return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form, })
