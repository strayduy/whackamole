# Third party libs
from flask import redirect, url_for, session
from flask import Blueprint
from flask import render_template
from flask import request

# Models
from ..models import SenateVote
from ..models import SenateRep

# Initialize blueprint
blueprint = Blueprint('root', __name__)

# TODO: Figure out how to pass two arguments here
@blueprint.route('/<state>')
def index(state=None):
  me = session.get('user')

  if not me:
    return redirect(url_for('oauth.login'))

  if state:
    state = state.upper()

  votes = SenateVote.get(rep_id=None, state=state)
  return render_template('index.html', name=me['name'],
      state=state, votes=votes)

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
  votes = SenateVote.get(rep_id=rep_id, state=None)
  return render_template('rep.html', rep=rep, votes=votes)
