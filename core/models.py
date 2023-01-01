from django.db.models import Model, CharField, URLField

# Create your models here.

class Movie(Model):
    title = CharField(max_length=99)
    video_url = URLField(max_length=9999999999999999999999999999999999999999999999999999999999999999999)


    
