import os
import secrets

SECRET_KEY = secrets.token_urlsafe(64)

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_NAME = 'flask_basics.db'
SQLALCHEMY_DATABASE_PATH = os.path.join(BASE_DIR, 'db', SQLALCHEMY_DATABASE_NAME)
SQLALCHEMY_DATABASE_URI = f'sqlite:///{SQLALCHEMY_DATABASE_PATH}'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True
