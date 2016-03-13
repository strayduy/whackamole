# Third party libs
from flask import Blueprint
from flask import render_template
from flask import request

# Initialize blueprint
blueprint = Blueprint('root', __name__)

@blueprint.route('/')
def index():
    variable = request.args.get('v')
    return render_template('index.html', variable=variable)

@blueprint.route('/bill')
def bill():
    return 'this is a bill'

