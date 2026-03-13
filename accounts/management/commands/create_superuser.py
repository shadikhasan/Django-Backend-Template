from argparse import RawTextHelpFormatter

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    DEFAULT_USERNAME = "admin"
    DEFAULT_EMAIL = "admin@example.com"
    DEFAULT_PASSWORD = "admin12345"

    help = "Create a superuser using hardcoded default credentials."
    manual = """Manual:
1) Create with hardcoded credentials:
   python3 manage.py create_superuser

2) Hardcoded credentials in this command:
   username: admin
   email: admin@example.com
   password: admin12345

3) Change default credentials:
   Edit DEFAULT_USERNAME, DEFAULT_EMAIL, DEFAULT_PASSWORD in:
   accounts/management/commands/create_superuser.py

4) Show this manual:
   python3 manage.py create_superuser --manual
"""

    def add_arguments(self, parser):
        parser.formatter_class = RawTextHelpFormatter
        parser.epilog = self.manual

        parser.add_argument(
            "--manual",
            action="store_true",
            help="Show usage manual for this command and exit.",
        )

    def handle(self, *args, **options):
        if options.get("manual"):
            self.stdout.write(self.manual)
            return

        user_model = get_user_model()

        username = self.DEFAULT_USERNAME
        email = self.DEFAULT_EMAIL
        password = self.DEFAULT_PASSWORD

        existing_user = user_model.objects.filter(username=username).first()
        if existing_user:
            self.stdout.write(
                self.style.WARNING(f"Superuser '{username}' already exists. Skipping.")
            )
            self.stdout.write("Credentials:")
            self.stdout.write(f"  username: {username}")
            self.stdout.write(f"  email: {email}")
            self.stdout.write(f"  password: {password}")
            return

        user_model.objects.create_superuser(
            username=username,
            email=email,
            password=password,
        )
        self.stdout.write(
            self.style.SUCCESS(f"Superuser '{username}' created successfully.")
        )
        self.stdout.write("Credentials:")
        self.stdout.write(f"  username: {username}")
        self.stdout.write(f"  email: {email}")
        self.stdout.write(f"  password: {password}")
