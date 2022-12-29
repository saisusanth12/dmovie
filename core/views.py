from django.shortcuts import render
from .models import Movie

# Create your views here.

from .models import Movie

def index(request):
    movies = Movie.objects.all()
    return render(request, 'index.html', {
        'movies':movies
    })