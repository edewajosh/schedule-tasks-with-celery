# This will ensure the app is always imported when
# Django starts so thar shared_task will use this app.
from picha.celery import app as celery_app

__all__ = ('celery_app')