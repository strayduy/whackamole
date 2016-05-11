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

@blueprint.route('/')
def index():
  me = session.get('user')

  if not me:
    return redirect(url_for('oauth.login'))

  votes= SenateVote.get_all()
  return render_template('index.html', name=me['name'],
      votes=votes)

@blueprint.route('/signout')
def signout():
    if session.get('user'):
        del session['user']
    return redirect(url_for('oauth.login'))

@blueprint.route('/state', methods=['POST'])
@blueprint.route('/state/<state>')
def state(state=None):
  me = session.get('user')

  if not me:
    return redirect(url_for('oauth.login'))

  if request.method == "POST":
    state = request.form['state']
  state = state.upper()
  votes = SenateVote.get_state(state)
  return render_template('state.html', name=me['name'],
      votes=votes, state=state)

@blueprint.route('/rep/<rep_id>')
def rep(rep_id):
  me = session.get('user')

  if not me:
    return redirect(url_for('oauth.login'))

  rep = SenateRep.get_by_rep_id(rep_id)
  votes = SenateVote.get_by_rep_id(rep_id)
  return render_template('rep.html', rep=rep, votes=votes)

