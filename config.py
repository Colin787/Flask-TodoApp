import os
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """Set Flask configuration vars."""

    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:peaches777@127.0.0.1:5432/TodoV2'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = os.urandom(32)

    SESSION_COOKIE_SECURE = True

    SESSION_COOKIE_NAME = 'Todo-App-Cookie'

    WTF_CSRF_TIME_LIMIT = None
