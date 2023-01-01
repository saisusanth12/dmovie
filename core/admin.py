from django.contrib import admin
from .models import Movie

# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'video_url')
    list_filter = ('title',)
    search_fields = ['title']

admin.site.register(Movie, MovieAdmin)