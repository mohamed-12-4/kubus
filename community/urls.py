from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.index, name="community_index"),
    path("create_post", view=views.create_post, name="create_post"),
    path("posts", view=views.posts, name="posts")
]