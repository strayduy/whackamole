# Third party libs
from bson.objectid import ObjectId
from flask import redirect, url_for, session
from flask import Blueprint
from flask import render_template
from flask import request

import simplejson as json

# Models
from ..models import SenateVote
from ..models import SenateRep
from ..models import UserVote

# Initialize blueprint
blueprint = Blueprint('root', __name__)

@blueprint.route('/')
@blueprint.route('/<string:state>')
@blueprint.route('/<string:state>/<string:user_id>')
def index(state=None, user_id=None):
  me = session.get('user')

  if not me:
    return redirect(url_for('oauth.login'))

  if state:
    state = state.upper()

  votes = SenateVote.get(rep_id=None, user_id=user_id, state=state)
  return render_template('index.html', name=me['name'],
      state=state, user_id=user_id, votes=votes)

@blueprint.route('/signout')
def signout():
    if session.get('user'):
        del session['user']
    return redirect(url_for('oauth.login'))

@blueprint.route('/rep/<rep_id>')
def rep(rep_id):
  me = session.get('user')

  if not me:
    return redirect(url_for('oauth.login'))

  rep = SenateRep.get_by_rep_id(rep_id)
  votes = SenateVote.get(rep_id=rep_id, user_id=None, state=None)
  return render_template('rep.html', rep=rep, votes=votes)

@blueprint.route('/inc', methods=['POST'])
def increment_count():
  vote_id = request.form['vote_id'].replace(" + ", "")
  consistent = int(request.form['consistent'])
  me = session.get('user')
  old_vote = UserVote.get(user_id=me["name"], vote_id=vote_id)
  if not old_vote:
    UserVote.add_vote(user_id=me["name"], vote_id=vote_id, consistent=consistent)
    SenateVote.update_vote(vote_id, consistent)
    operation = "increment"
  else:
    UserVote.delete(user_id=me["name"], vote_id=vote_id)
    SenateVote.update_vote(vote_id, old_vote["consistent"], -1)
    operation = "decrement"
  return json.dumps({'status':'OK','operation':operation})

@blueprint.route('/clear_votes', methods=['POST'])
def clear_votes():
  vote_id = request.form['vote_id'].replace(" + ", "")
  me = session.get('user')
  SenateVote.clear_votes(vote_id)
  UserVote.delete(user_id=None, vote_id=vote_id)
  return json.dumps({'status':'OK','vote_id':vote_id})

@blueprint.route('/clear_user', methods=['POST'])
def clear_user():
  user_id = request.form['user_id']
  me = session.get('user')
  votes = UserVote.get(user_id=user_id, vote_id=None)
  for vote in votes:
    SenateVote.update_vote(vote["congress_vote_id"], vote["consistent"], -1)
  UserVote.delete(user_id=user_id, vote_id=None)
  return json.dumps({'status':'OK','user_id':user_id})

