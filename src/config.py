import os
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secretkeysample'
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:password@mariadb/flask_blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
