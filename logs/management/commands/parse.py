from django.core.management import BaseCommand
import logs.parser as p


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('urls', nargs='+', type=str)

    def handle(self, *args, **options):
        count = 0
        for url in options['urls']:
            p.download_file(url)
            self.stdout.write(self.style.SUCCESS(f'Log file {url} was successfully downloaded'))
            p.parse_apache_log_file()
            p.delete_file()
            count += 1
        self.stdout.write(self.style.SUCCESS(f'{count} files were parsed'))
