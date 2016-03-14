# Third party libs
import pymongo

class Database(object):
    db = None

    @classmethod
    def connect(cls, **config):
        client = pymongo.MongoClient(config['host'])
        db = client[config['name']]
        if config.get('user') and config.get('password'):
            db.authenticate(config['user'], config['password'])
        cls.db = db

