import csv
from django.core.management.base import BaseCommand
from api.models import Movie  

class Command(BaseCommand):
    help = 'Import movies from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file to be imported')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        try:
            with open(csv_file, newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                headers = reader.fieldnames
                expected_headers = {'tconst', 'originalTitle'}
                if not expected_headers.issubset(headers):
                    self.stdout.write(self.style.ERROR('CSV file is missing required headers.'))
                    return

                movie_count = 0
                for row in reader:
                    imdb_id = row['tconst']
                    title = row['originalTitle']
                    # Set is_active to False and other optional fields to None or empty strings
                    movie, created = Movie.objects.update_or_create(
                        imdb_id=imdb_id,
                        defaults={
                            'title': title,
                            'year': None,
                            'genres': '',
                            'director': '',
                            'is_active': False,
                        }
                    )
                    if created:
                        movie_count += 1
                self.stdout.write(self.style.SUCCESS(f'Successfully imported {movie_count} movies'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'File "{csv_file}" not found.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An error occurred: {e}'))