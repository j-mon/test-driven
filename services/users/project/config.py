# services/users/project/config.py


import os # new 


class BaseConfig:
    """Base configuration"""
    Testing = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False # new
    SECRET_KEY = 'my_precious' # new 


class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') # new


class TestingConfig(BaseConfig):
    """Testing configuration"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_TEST_URL') # new


class ProductionConfig(BaseConfig):
    """Production configurstion"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') # new


