from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .form import *

# Create your views here.
def index(request):
    return render(request, "main/index.html")

def logoutUser(request):
    logout(request)
    return redirect("home")

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try :
            user = User.objects.get(username=username)
        except :
            messages.error(request, "User not exists")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Username Or password is not correct")
    return render(request, "main/login.html")

def register_user(request):
    form = UserRegister()

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'main/register.html', {'form': form})