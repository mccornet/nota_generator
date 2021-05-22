import os
basedir = os.path.abspath(os.path.dirname(__file__))

database_name = "data.db"

class Config(object):
    # form settings
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # Database settings
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("://", "ql://", 1) or \
    'sqlite:///' + os.path.join(basedir, database_name)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
