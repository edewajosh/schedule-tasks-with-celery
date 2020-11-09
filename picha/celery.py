# from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from celery.schedules import crontab
# from photos import tasks


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'picha.settings')

app = Celery('picha')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    "task-save-latest-flickr-image": {
        "task": "task_save_latest_flickr_image",
        "schedule": crontab(minute='*/10'),
        "args": (),
    }
}

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')