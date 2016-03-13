# Third party libs
from flask import Blueprint

# Initialize blueprint
blueprint = Blueprint('root', __name__)

@blueprint.route('/')
def index():
    return 'hello world'

