import pymongo

class MongoConnector:
    def __init__(self, host='localhost', port=27017, db='myDB'):
        self.client = None
        self.host = host
        self.port = port
        self.db = db

    def connect(self):
        self.client = pymongo.MongoClient(self.host, self.port)
        return self.client[self.db]

    def close(self):
        self.client.close()
