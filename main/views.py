from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .form import *
from .models import *
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view

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

@login_required(login_url='login')
def buses(request):
    user = request.user
    trips = Schedule.objects.filter(students=user)
    print(trips)
    return render(request, "main/buses.html", {"trips": trips})


def register_user(request):
    form = UserRegister()

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            _ = Points.objects.create(student=user, value=0)
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'main/register.html', {'form': form})

def commit_list(request):
    trips = Schedule.objects.all()
    return render(request, "main/commit_list.html", {"trips": trips})

@login_required(login_url='login')
def commit(request, bus_id):
    if request.method == "POST":
        _ = Schedule.objects.get(id=bus_id).students.add(request.user)
        return redirect("buses")

@api_view(['POST'])
def attend_api(request):
    user = request.user
    _ = Attendance.objects.create(student=user)
    p = Points.objects.get(student=user)
    p.value += 1
    p.save()
    return render(request, "main/attend.html", {"points": p.value})

@login_required(login_url='login')
def attend(request):
    if request.method == "POST":
        user = request.user
        _ = Attendance.objects.create(student=user)
        points = Points.objects.get(student=user).value
        return render(request, "main/attend.html", {"points": points})