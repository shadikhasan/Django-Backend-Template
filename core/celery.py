import os

from celery import Celery
from dotenv import load_dotenv

load_dotenv()
django_env = os.getenv("DJANGO_ENV", "dev")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"core.settings.{django_env}")

app = Celery('core')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
