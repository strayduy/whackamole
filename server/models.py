# Standard libs
import random

# Third party libs
from bson.objectid import ObjectId
import pymongo

# Our libs
from .database import Database

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

class SenateVote(object):
  def __init__(self, data):
    self.id = data['_id']
    self.bill_title = data['bill_title']
    self.rep_state = data['rep_state']
    self.outcome = data['outcome']
    self.rep_name = data['rep_name']

  @classmethod
  def get_all(cls):
    senate_votes = Database.db.senate_votes.find({'rep_state': 'CA'})
    senate_votes = map(SenateVote, senate_votes)
    return senate_votes

