# Third party libs
from flask import redirect, url_for, session
from flask_oauth import OAuth
from flask import Blueprint
from flask import request

# Models
from ..settings import Config

oauth = OAuth()

facebook = oauth.remote_app('facebook',
    base_url='https://graph.facebook.com/',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
    consumer_key=Config.FACEBOOK_APP_ID,
    consumer_secret=Config.FACEBOOK_APP_SECRET,
    request_token_params={'scope': 'email'}
)

# Initialize blueprint
blueprint = Blueprint('oauth', __name__, url_prefix='/oauth')

@blueprint.route('/login')
def login():
  return facebook.authorize(callback=url_for('oauth.facebook_authorized',
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
  session['user'] = {
    'name': facebook.get('/me').data['name'],
  }
  return redirect(url_for('root.index'))

@facebook.tokengetter
def get_facebook_oauth_token():
  return session.get('oauth_token')

