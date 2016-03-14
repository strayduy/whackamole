# Standard libs
import os

class Config(object):
    DEBUG = True
    SECRET_KEY = os.getenv('SECRET_KEY', 'replace_me_in_production')

    WHACKAMOLE_DB_HOST = os.getenv('WHACKAMOLE_DB_HOST')
    WHACKAMOLE_DB_NAME = os.getenv('WHACKAMOLE_DB_NAME')
    WHACKAMOLE_DB_USER = os.getenv('WHACKAMOLE_DB_USER')
    WHACKAMOLE_DB_PASSWORD = os.getenv('WHACKAMOLE_DB_PASSWORD')

