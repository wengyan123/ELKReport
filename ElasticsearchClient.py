from elasticsearch import Elasticsearch


class ElasticsearchClient:
    _host = 'localhost:9200'
    _index = 'filebeat-*'
    _size = '10000'
    _sort = '@timestamp:asc'

    def __init__(self, **kwargs):
        if 'host' in kwargs:
            self._host = kwargs['host']
        self.client = Elasticsearch(self._host)


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

        messages = []
        for hit in response['hits']['hits']:
            messages.append(hit['_source']['message'])

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
                {"range": {"@timestamp": {"gte": "2018-08-16", "lte": "2018-08-17"}}}
              ]
            }
          }
        }
    messages = client.search(dsl)
    for msg in messages:
        print msg
