# Third party libs
from flask import Flask, redirect, url_for, session
from flask_oauth import OAuth
from flask import Blueprint
from flask import render_template
from flask import request

# Models
from ..models import SenateVote
from ..models import SenateRep
from ..settings import Config

SECRET_KEY = 'development key'
DEBUG = True
FACEBOOK_APP_ID = Config.FACEBOOK_APP_ID
FACEBOOK_APP_SECRET = Config.FACEBOOK_APP_SECRET

app = Flask(__name__)
app.debug = DEBUG
app.secret_key = SECRET_KEY
oauth = OAuth()

facebook = oauth.remote_app('facebook',
    base_url='https://graph.facebook.com/',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
    consumer_key=FACEBOOK_APP_ID,
    consumer_secret=FACEBOOK_APP_SECRET,
    request_token_params={'scope': 'email'}
)


# Initialize blueprint
blueprint = Blueprint('root', __name__)

@blueprint.route('/')
def index():
  return redirect(url_for('root.login'))

@blueprint.route('/login')
def login():
  return facebook.authorize(callback=url_for('root.facebook_authorized',
      next=request.args.get('next') or request.referrer or None,
      _external=True))

@blueprint.route('/login/authorized')
@facebook.authorized_handler
def facebook_authorized(resp):
  if resp is None:
    return 'Access denied: reason=%s error=%s' % (
        request.args['error_reason'],
        request.args['error_description']
    )
  session['oauth_token'] = (resp['access_token'], '')
  me = facebook.get('/me')
  votes= SenateVote.get_all()
  return render_template('index.html', name=me.data['name'],
      votes=votes)

@facebook.tokengetter
def get_facebook_oauth_token():
  return session.get('oauth_token')

@blueprint.route('/state', methods=['POST'])
@blueprint.route('/state/<state>')
def state(state=None):
  me = facebook.get('/me')
  if request.method == "POST":
    state = request.form['state']
  state = state.upper()
  votes = SenateVote.get_state(state)
  return render_template('state.html', name=me.data['name'],
      votes=votes, state=state)

@blueprint.route('/rep/<rep_id>')
def rep(rep_id):
  rep = SenateRep.get_by_rep_id(rep_id)
  votes = SenateVote.get_by_rep_id(rep_id)
  return render_template('rep.html', rep=rep, votes=votes)
