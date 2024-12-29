from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#movie model
class Movie(models.Model):
    title = models.CharField(max_length=255)  # Movie title
    year = models.IntegerField()  # Release year
    imdb_id = models.CharField(max_length=20, unique=True)  # IMDb ID for unique identification
    poster = models.URLField(null=True, blank=True)  # URL to the movie's poster
    last_updated = models.DateTimeField(auto_now=True)  # Tracks when the record was last updated

    def __str__(self):
        return self.title
    
#review model
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    submit_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.user.username} for {self.movie.title}'