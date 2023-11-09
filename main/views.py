from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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