# Third party libs
from flask import Flask

# Our libs
from .database import Database

# Blueprints
from .blueprints import root

def create_app(config_object):
    app = Flask(__name__, static_folder='../client/static')
    app.config.from_object(config_object)

    # Connect to database
    db_config = {
        'host': app.config.get('WHACKAMOLE_DB_HOST', ''),
        'name': app.config.get('WHACKAMOLE_DB_NAME', ''),
        'user': app.config.get('WHACKAMOLE_DB_USER', ''),
        'password': app.config.get('WHACKAMOLE_DB_PASSWORD', ''),
    }
    Database.connect(**db_config)

    app.register_blueprint(root.blueprint)

    return app

