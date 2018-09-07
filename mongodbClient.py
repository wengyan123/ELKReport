from pymongo import MongoClient


class MongodbClient:
    _host = 'mongodb://192.168.16.136:27017'
    _db_name = 'elk'
    _collection = 'reports'

    def __init__(self, **kwargs):
        if 'host' in kwargs:
            self._host = kwargs['host']
        if 'db' in kwargs:
            self._db = kwargs['db']
        self.client = MongoClient(self._host)
        self.db = self.client[self._db_name]

    def storeReport(self, data, collection=_collection):
        reports = self.db[collection]
        result = reports.insert_one(data)
        print('One post: {0}'.format(result.inserted_id))
