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
  def get(cls, rep_id, user_id, state):
    find_dict = {}
    if rep_id:
      find_dict['rep_id'] = rep_id
    if state:
      find_dict['rep_state'] = state
    if user_id:
      user_votes = Database.db.user_votes.find({'user_id':user_id})
      vote_oids = [ObjectId(v['congress_vote_id']) for v in user_votes]
      find_dict['_id'] = {'$in':vote_oids}
    votes = Database.db.senate_votes.find(find_dict).sort('downvotes',
        pymongo.DESCENDING)
    votes = map(SenateVote, votes)
    return votes

  @classmethod
  def update_vote(cls, vote_id, consistent, increment=1):
    counter = "upvotes"
    if not consistent:
      counter = "downvotes"
    inc_dict = {"$inc": {counter: increment}}
    Database.db.senate_votes.update(
      {"_id": ObjectId(vote_id)},
      inc_dict
    )

  @classmethod
  def clear_votes(cls, vote_id):
    Database.db.senate_votes.update(
      {"_id": ObjectId(vote_id)},
      {"$set": {"upvotes":0, "downvotes":0}}
    )

class UserVote(object):
  def __init__(self, data):
    self.id = data['_id']
    self.user_id = data['user_id']
    self.vote_id = data['vote_id']
    self.consistent = data['consistent']

  @classmethod
  def get(cls, user_id=None, vote_id=None):
    find_dict = {}
    if user_id:
      find_dict['user_id'] = user_id
    if vote_id:
      find_dict['congress_vote_id'] = vote_id
    if user_id and vote_id:
      return Database.db.user_votes.find_one(find_dict)
    return  Database.db.user_votes.find(find_dict)

  @classmethod
  def add_vote(cls, user_id, vote_id, consistent):
    insert_dict = {
      "user_id":user_id,
      "congress_vote_id":vote_id,
      "consistent":consistent
    }
    Database.db.user_votes.insert(insert_dict)

  @classmethod
  def delete(cls, user_id, vote_id):
    delete_dict = {}
    if user_id:
      delete_dict["user_id"] = user_id
    if vote_id:
      delete_dict["congress_vote_id"] = vote_id
    Database.db.user_votes.remove(delete_dict)
