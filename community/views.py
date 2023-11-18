from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Posts
# Create your views here.
def index(request):
    return render(request, "community/index.html")

@login_required(login_url='login')
def create_post(request):
    if request.method =="POST":
        notes = request.POST.get("notes")
        _ = Posts.objects.create(author=request.user,
                                 notes=notes)
        return redirect("community_index")
    return render(request, "community/add_post.html")

@login_required(login_url='posts')
def posts(request):
    posts = Posts.objects.all()
    return render(request, "community/view_posts.html", {"posts":posts})