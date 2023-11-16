from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("logout", views.logoutUser, name="logout"),
    path("login", views.loginUser, name="login"),
    path("sign-up", view=views.register_user, name="sign-up"),
    path("buses", views.buses, name="buses"),
    path("attend", view=views.attend_api, name="attend-api"),
    path("congrats", view=views.attend, name="attend"),
    path("commit_list/", view=views.commit_list, name="commit"),
    path("commit/<int:bus_id>", view=views.commit, name="commit")
]