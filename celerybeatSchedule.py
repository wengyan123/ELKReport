from datetime import timedelta
from celery.schedules import crontab

dsl = {
          "query": {
            "bool": {
              "must": [
                {"match": {"beat.hostname": "ubuntu"}},
                {"match": {"source": "/var/log/auth.log"}},
                {"match": {"message": "wengyan"}}
              ],
              "filter": [
                {"range": {"@timestamp": {"gte": "2018-08-19", "lte": "2018-08-20"}}}
              ]
            }
          }
        }


CELERYBEAT_SCHEDULE = {
    'add-every-5-seconds': {
        'task': 'watcher.add',
        'schedule': timedelta(seconds=600),
        'args': (16, 16)
    },
    'generate-elk-report': {
        'task': 'watcher.genReport',
        'schedule': timedelta(seconds=10),
        'args': (dsl,)
    },
}
