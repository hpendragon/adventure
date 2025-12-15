import os

SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-please-change'
DEBUG = True
