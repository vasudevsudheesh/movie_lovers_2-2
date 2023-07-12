from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .models import Movie
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

from django.shortcuts import render, redirect
from .forms import MovieForm
from django.shortcuts import get_object_or_404, redirect, render
from .models import Movie
from django.shortcuts import render, get_object_or_404


# views.py
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, "movie_list.html", {"movies": movies})


def edit_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect("movie_list")
    else:
        form = MovieForm(instance=movie)

    return render(request, "edit_movie.html", {"form": form})


def delete_movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)

    if request.method == "POST":
        movie.delete()
        return redirect("index")

    context = {"movie": movie}
    return render(request, "delete_movie.html", context)


def add_movie(request):
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = MovieForm()

    return render(request, "add_movie.html", {"form": form})


def index(request):
    # form = SignUpForm()
    movie = Movie.objects.all()
    context = {"movie_list": movie}
    return render(request, "index.html", context)


def movie_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, "movie_detail.html", {"movie": movie})


# views.py


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("index")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("login")


def movie_list(request):
    movies = Movie.objects.all()
    return render(request, "movie_list.html", {"movies": movies})
