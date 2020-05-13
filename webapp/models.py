from django.db import models

# Create your models here.

# This is a Movie object that will be stored in the DB
class Movie(models.Model):
    movie_id = models.CharField(max_length=1000)
    name = models.CharField(max_length=1000)
    duration = models.IntegerField()
    cover_photo = models.CharField(max_length=10000, default='https://www.voiceofsandiego.org/wp-content/uploads/2013/08/film081513.jpg')

    def __str__(self):
        return self.name