# Third party libs
from flask import Blueprint
from flask import render_template
from flask import request

# Models
from ..models import Vote

# Initialize blueprint
blueprint = Blueprint('root', __name__)

@blueprint.route('/')
def index():
    votes = [Vote() for _ in xrange(10)]
    return render_template('index.html', votes=votes)

@blueprint.route('/bill/<bill_id>')
def bill(bill_id):
    return 'this is a bill #' + bill_id

