from celery import Celery

from elasticsearchClient import ElasticsearchClient
from mongodbClient import MongodbClient


app = Celery('Watcher')
app.config_from_object('celeryconfig')


@app.task
def genReport(dsl):
    elastic_client = ElasticsearchClient()
    print(dsl)
    messages = elastic_client.search(dsl)
    #for msg in messages:
    #    print msg
    storeReport.delay(messages)


@app.task
def storeReport(messages):
    mongodb_client = MongodbClient()
    mongodb_client.putReport(messages)
