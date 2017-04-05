import os

SECRET_KEY = 'development key' # keep this key secret during production
SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/easecentral'
SQLALCHEMY_TRACK_MODIFICATIONS = False
DEBUG = True