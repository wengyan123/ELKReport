from datetime import timedelta
from celery.schedules import crontab

CELERYBEAT_SCHEDULE = {
    'add-every-5-seconds': {
        'task': 'watcher.add',
        'schedule': timedelta(seconds=5),
        'args': (16, 16)
    },
    'add-every-monday-morning': {
        'task': 'watcher.add',
        'schedule': crontab(hour=13, minute=34, day_of_week=3),
        'args': (1, 1),
    },
}