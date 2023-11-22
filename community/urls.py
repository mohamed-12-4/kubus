from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.index, name="community_index"),
    path("create_post", view=views.create_post, name="create_post"),
    path("posts", view=views.posts, name="posts"),
    path("article_list", view=views.articles_list, name="article_list"),
    path("article/<int:pk>", view=views.article, name="article"),
    path("add_article", view=views.add_article, name="add_article"),
]