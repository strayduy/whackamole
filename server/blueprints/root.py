# Third party libs
from flask import Blueprint
from flask import render_template
from flask import request

# Models
from ..models import Bill
from ..models import Vote

# Initialize blueprint
blueprint = Blueprint('root', __name__)

@blueprint.route('/')
def index():
    votes = Vote.get_all()
    return render_template('index.html', votes=votes)

@blueprint.route('/bill/<bill_id>')
def bill(bill_id):
    bill = Bill.get_by_id(bill_id)
    return bill['title'] + '<br>' + bill['description']

