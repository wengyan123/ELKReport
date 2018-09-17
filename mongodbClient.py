from pymongo import MongoClient


class MongodbClient:
    _host = 'mongodb://192.168.107.128:27017'
    _db_name = 'elk'
    _collection = 'reports'

    def __init__(self, **kwargs):
        if 'host' in kwargs:
            self._host = kwargs['host']
        if 'db' in kwargs:
            self._db = kwargs['db']
        self.client = MongoClient(self._host)
        self.db = self.client[self._db_name]

    def putReport(self, document, collection=_collection):
        reports = self.db[collection]
        result = reports.insert_one(document)
        print('Report ID: {0}'.format(result.inserted_id))
