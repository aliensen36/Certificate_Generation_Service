import json
import os
from django.core.management.base import BaseCommand
from django.core.management import call_command
from io import StringIO


class Command(BaseCommand):
    help = 'Экспортирует данные в файл JSON только для приложения certificates'

    def handle(self, *args, **kwargs):
        export_dir = '/usr/src/app/CGS/data'
        file_path = os.path.join(export_dir, 'data.json')
        output = StringIO()
        call_command('dumpdata', 'certificates', '--indent', '4', stdout=output)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(output.getvalue())

        self.stdout.write(self.style.SUCCESS(f'Данные успешно экспортированы в {file_path}'))
