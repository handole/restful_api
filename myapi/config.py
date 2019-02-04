"""Default configuration

Use env var to override
"""
import os
import psycopg2

DEBUG = True
SECRET_KEY = "changeme"

# DATABASE_URL = os.environ.url['DATABASE_URL']
# conn = psycopg2.connect(DATABASE_URL, sslmode='require')
# SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/myapi.db"
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://postgres:ho555iv020@localhost:5432/apitwit' or "sqlite:////tmp/myapi.db"
SQLALCHEMY_TRACK_MODIFICATIONS = False

JWT_BLACKLIST_ENABLED = True
JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
CELERY_BROKER_URL = "amqp://guest:guest@localhost/"
CELERY_RESULT_BACKEND = "amqp://guest:guest@localhost/"
