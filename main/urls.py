from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("logout", views.logoutUser, name="logout"),
    path("login", views.loginUser, name="login"),
    path("sign-up", view=views.register_user, name="sign-up")
]