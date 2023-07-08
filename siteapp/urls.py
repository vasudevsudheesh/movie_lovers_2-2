from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("movie/<int:movie_id>", views.movie_detail, name="movie_detail"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("add_movie", views.add_movie, name="add_movie"),
    path("movies/<int:movie_id>/delete/", views.delete_movie, name="delete_movie"),
]
git config --global user.email "sudheeshyft@gmail.com.com"
git config --global user.name "sudheesh vasudev"