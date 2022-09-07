import os

from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "course4_proj.settings")
os.environ.setdefault("DJANGO_CONFIGURATION", "Dev")

import configurations

configurations.setup()

app = Celery("course4_proj")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html
# https://github.com/celery/celery/tree/master/celery
# https://github.com/celery/django-celery-beat/tree/master/django_celery_beat
# https://github.com/celery/django-celery-beat/blob/master/django_celery_beat/models.py
# https://github.com/celery/django-celery-beat/blob/d4b97af62889527582194f3932e013ad972a88b3/django_celery_beat/schedulers.py
# https://github.com/celery/django-celery-results/tree/master/django_celery_results
# https://crontab.guru/