# Standard libs
import random

# Third party libs
from bson.objectid import ObjectId
import pymongo

# Our libs
from .database import Database

class Bill(object):
    @classmethod
    def get_by_id(cls, _id):
        bill = Database.db.bills.find_one({'_id': ObjectId(_id)})
        return bill

class Vote(object):
    def __init__(self, data):
        self.id = data['_id']
        self.representative = data['representative']
        self.decision = data['decision']
        self.bill_id = data['bill_id']

        self.bill = Database.db.bills.find_one({'_id': ObjectId(data['bill_id'])})

    @classmethod
    def get_all(cls):
        votes = Database.db.votes.find({'representative': 'Alice'})
        votes = map(Vote, votes)
        return votes

