from celerybeatSchedule import CELERYBEAT_SCHEDULE

# http://docs.celeryproject.org/en/latest/userguide/configuration.html
#BROKER_URL = 'pyamqp://guest@localhost//'
BROKER_URL = 'redis://localhost/0'
CELERY_RESULT_BACKEND = 'redis://localhost/1'

CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT=['json']
CELERY_TIMEZONE = 'Asia/Shanghai'

CELERYBEAT_SCHEDULE = CELERYBEAT_SCHEDULE
