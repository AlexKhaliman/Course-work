import json
import os

from django.core.management import BaseCommand
from django.conf import settings
from categories.models import Categories, Tasks

SEED_FILE = os.path.join(
    settings.BASE_DIR,
    'static',
    'tasks.json'
)


class Command(BaseCommand):
    help = 'Populates the database with seed data'

    def add_arguments(self, parser):
        parser.add_argument('--truncate', '-t', default=False, action='store_true')

    def handle(self, *args, **options):
        if options['truncate']:
            Tasks.objects.all().delete()

        with open(SEED_FILE) as f:
            categories = json.load(f)

        bulk_tasks = []
        for cat in categories:
            bulk_tasks.append(
                Tasks(
                    name=cat['name'],
                    comments=cat['comments'],
                    price=cat['price'],
                    category=cat['category']
                )
            )
            self.stdout.write(f" {cat['name']} processed")

        Tasks.objects.bulk_create(bulk_tasks)
