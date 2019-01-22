"""Default configuration

Use env var to override
"""
import os

DEBUG = True
SECRET_KEY = "changeme"

# SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/myapi.db"
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://postgres:ho555iv020@localhost:5432/stackcamp' or "sqlite:////tmp/myapi.db"
SQLALCHEMY_TRACK_MODIFICATIONS = False

JWT_BLACKLIST_ENABLED = True
JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
CELERY_BROKER_URL = "amqp://guest:guest@localhost/"
CELERY_RESULT_BACKEND = "amqp://guest:guest@localhost/"
