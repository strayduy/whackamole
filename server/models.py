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

class SenateRep(object):
  def __init__(self, data):
    self.id = data['_id']
    self.senate_id = data['rep_id']
    self.senate_name = data['rep_name']
    self.state = data['state']
    self.yes_votes = data['yes_votes']
    self.no_votes = data['no_votes']
    self.abstain_votes = data['abstain_votes']
    self.upvotes = data['upvotes']
    self.downvotes = data['downvotes']

  @classmethod
  def get_by_rep_id(cls, rep_id):
    senate_rep = Database.db.senate_reps.find_one({'rep_id': rep_id})
    return senate_rep

class SenateVote(object):
  def __init__(self, data):
    self.id = data['_id']
    self.bill_title = data['bill_title']
    self.bill_link = data['bill_link']
    self.rep_state = data['rep_state']
    self.outcome = data['outcome']
    self.rep_name = data['rep_name']
    self.rep_id = data['rep_id']
    self.upvotes = data['upvotes']
    self.downvotes = data['downvotes']

  @classmethod
  def get(cls, rep_id, state):
    find_dict = {}
    if rep_id:
      find_dict['rep_id'] = rep_id
    if state:
      find_dict['rep_state'] = state
    votes = Database.db.senate_votes.find(find_dict).sort('downvotes',
        pymongo.DESCENDING)
    votes = map(SenateVote, votes)
    return votes
