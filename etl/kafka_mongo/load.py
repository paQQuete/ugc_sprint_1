from pymongo import MongoClient


class MongoLoad:
    def __init__(self, topic: str, data: dict, mongo_host: str, mongo_port: int = 27019, database: str = 'dataBase'):
        self._topic = topic
        self._database = database
        self._data = data
        self._client = MongoClient(mongo_host, mongo_port)
        self._db_client = self._checkout_database()
        self._db_collection = self._checkout_collection()
        self._inserted_one_resp = self._insert_one()

    def _checkout_database(self):
        return self._client[self._database]

    def _checkout_collection(self):
        return self._db_client[self._topic]

    def _insert_one(self):
        return self._db_collection.insert_one(self._data)

    @property
    def inserted_one(self):
        return self._inserted_one_resp.inserted_id
