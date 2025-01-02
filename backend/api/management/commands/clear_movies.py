from django.core.management.base import BaseCommand
from api.models import Movie  # Replace 'api' with your app name

class Command(BaseCommand):
    help = 'Delete all Movie records from the database'

    def handle(self, *args, **kwargs):
        deleted_count, _ = Movie.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(f'Successfully deleted {deleted_count} movies'))