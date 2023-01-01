from django.shortcuts import render
from .models import Movie

# Create your views here.

def index(req):
    movies = Movie.objects.all()
    return render(req, 'index.html', {'movies' : movies})
