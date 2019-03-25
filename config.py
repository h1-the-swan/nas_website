import sys, os
from dotenv import load_dotenv, find_dotenv
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    """Configuration object for Flask app"""

    # def __init__(self):
    #     """TODO: to be defined1. """

    APP_NAME = os.environ.get('APP_NAME') or ''
    if os.environ.get('SECRET_KEY'):
        SECRET_KEY = os.environ.get('SECRET_KEY')
    else:
        SECRET_KEY = 'SECRET_KEY_ENV_VAR_NOT_SET'
        print('SECRET KEY ENV VAR NOT SET! SHOULD NOT SEE IN PRODUCTION')

class DevelopmentConfig(Config):

    # def __init__(self):
    #     """TODO: to be defined1. """
    #     Config.__init__(self)

    DEBUG = True
    print('THIS APP IS IN DEBUG MODE. YOU SHOULD NOT SEE THIS IN PRODUCTION.')

class ProductionConfig(Config):

    # def __init__(self):
    #     """TODO: to be defined1. """
    #     Config.__init__(self)

    DEBUG = False
        

        
        
