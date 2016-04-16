# Third party libs
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
    state = 'FL'
    votes = SenateVote.get_state(state)
    return render_template('index.html', votes=votes, state=state)

@blueprint.route('/rep/<rep_id>')
def rep(rep_id):
    rep = SenateRep.get_by_rep_id(rep_id)
    return render_template('rep.html', rep=rep)
