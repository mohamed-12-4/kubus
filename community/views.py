from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
from .models import *
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

@login_required(login_url='login')
def posts(request):
    posts = Posts.objects.all()
    return render(request, "community/view_posts.html", {"posts":posts})


@login_required(login_url='login')
def articles_list(request):
    articles = Articles.objects.all()
    return render(request, "community/articles.html", {"articles": articles})

@login_required(login_url='login')
def article(request, pk):
    article = Articles.objects.get(pk=pk)
    return render(request, "community/article.html", {"article": article})
@login_required(login_url='login')
def add_article(request):
    if request.method =="POST":
        form = ArticleForm(request.POST)
        if form.is_valid:
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect("article_list")
    form = ArticleForm()
    return render(request, "community/add_article.html", {"form": form})