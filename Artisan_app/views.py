from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterForm
# Create your views here.


def home(request):
    context = {}
    return render(request, 'Artisan_app/index.html', context)


def signup(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('confirmPassword')

        if len(password) < 8 and password.isalnum() is False and username == password:
            messages.error(request, "Try another password")

        if password == password2:

            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists try with a different one!')

            else:
                user = User.objects.create_user(username=username, password=password)
                login(request, user)
                return redirect('home')
        else:
            messages.error(request, 'Password did not match')

    return render(request, 'Artisan_app/signup.html')


def loginUser(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.get(username=username) is None:
            messages.error(request, 'User Doest Not exists!')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'incorrect username or password')
    return render(request, 'Artisan_app/login.html')


def logoutUser(request):

    logout(request)
    return redirect('home')
