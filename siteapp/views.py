from django.shortcuts import render
from . models import Movie
from django.http import HttpResponse
# Create your views here.


def index(request):
    movie = Movie.objects.all()
    context = {
        'movie_list': movie

    }
    return render(request, 'index.html', context)


def movie_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'movie_detail.html', {'movie': movie})
