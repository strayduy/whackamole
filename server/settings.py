# Standard libs
import os

class Config(object):
    DEBUG = True
    SECRET_KEY = os.getenv('SECRET_KEY', 'replace_me_in_production')

