from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.urls import reverse
import datetime

# Create your models here.
#movie model
class Movie(models.Model):
    title = models.CharField(
        max_length=255,
        help_text='Enter the movie title'
    )
    year = models.PositiveIntegerField(
        validators=[MaxValueValidator(datetime.date.today().year)],
        help_text='Enter the release year of the movie',
        blank=True,  # Field is optional
        null=True    # Allows storing NULL in the database
    )
    imdb_id = models.CharField(
        max_length=20,
        unique=True,
        help_text='Unique IMDb identifier'
    )
    genres = models.CharField(
        max_length=255,
        help_text='Comma-separated list of genres',
        blank=True  # Field is optional
    )
    director = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text='Director of the movie'
    )
    last_updated = models.DateTimeField(
        auto_now=True,
        help_text='The date and time when the record was last updated'
    )
    is_active = models.BooleanField(
        default=True,
        help_text='Indicates if the movie is active in the database'
    )

    def __str__(self):
        return f"{self.title} ({self.year})"

    def get_absolute_url(self):
        return reverse('movie_detail', args=[str(self.id)])

    class Meta:
        ordering = ['-year', 'title']
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'
    
#review model
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    submit_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.user.username} for {self.movie.title}'