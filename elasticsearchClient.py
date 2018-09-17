from elasticsearch import Elasticsearch

from mongodbClient import MongodbClient


class ElasticsearchClient:
    _host = 'localhost:9200'
    _index = 'filebeat-*'
    _size = '10000'
    _sort = '@timestamp:asc'

    def __init__(self, **kwargs):
        if 'host' in kwargs:
            self._host = kwargs['host']
        self.client = Elasticsearch(self._host)

    # https://elasticsearch-py.readthedocs.io/en/master/api.html?highlight=search()#elasticsearch.Elasticsearch.search
    def search(self, dsl, **kwargs):
        if 'index' in kwargs:
            self._index = kwargs['index']
        if 'size' in kwargs:
            self._size = kwargs['size']
        if 'sort' in kwargs:
            self._sort = kwargs['sort']

        response = self.client.search(
            index=self._index,
            size=self._size,
            sort=self._sort,
            body=dsl
        )

        messages = {}
        for hit in response['hits']['hits']:
            #messages[hit['_source']['@timestamp'][:-5]] = hit['_source']['message']
            message = {}
            message_id = hit['_id']
            message['timestamp'] = hit['_source']['@timestamp']
            message['content'] = hit['_source']['message']
            messages[message_id] = message
        return messages


if __name__ == '__main__':
    client = ElasticsearchClient()
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
    messages = client.search(dsl)

    mongodb_client = MongodbClient()
    mongodb_client.putReport(messages)
