from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=1000)
    video_url = models.URLField(max_length=100000000000000000000000000000, help_text='Enter your url here..')
    trailer_url = models.URLField(max_length=100000000, help_text='Enter here..', default='')