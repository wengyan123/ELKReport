from celery import Celery

from elasticsearchClient import ElasticsearchClient



app = Celery('Watcher')
app.config_from_object('celeryconfig')


@app.task
def genReport(dsl):
    client = ElasticsearchClient()
    print(dsl)
    messages = client.search(dsl)
    for msg in messages:
        print msg
