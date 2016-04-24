# Standard libs
import os

class Config(object):
    DEBUG = True
    SECRET_KEY = os.getenv('SECRET_KEY', 'replace_me_in_production')

    WHACKAMOLE_DB_HOST = os.getenv('WHACKAMOLE_DB_HOST')
    WHACKAMOLE_DB_NAME = os.getenv('WHACKAMOLE_DB_NAME')
    WHACKAMOLE_DB_USER = os.getenv('WHACKAMOLE_DB_USER')
    WHACKAMOLE_DB_PASSWORD = os.getenv('WHACKAMOLE_DB_PASSWORD')

    # Since the app is not yet published, using test settings from
    # github.com/mitsuhiko/flask-oauth/blob/master/example/facebook.py
    FACEBOOK_APP_ID = os.getenv('FACEBOOK_APP_ID', '188477911223606')
    FACEBOOK_APP_SECRET = os.getenv('FACEBOOK_APP_SECRET',
        '621413ddea2bcc5b2e83d42fc40495de')
