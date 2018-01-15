import os

class Config(object):
    """Base configuration."""

    SECRET_KEY = os.environ.get('APP_SECRET', 'SET IN DOCKER ENV')
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''
    DESTINATION_EMAIL = ''


class ProdConfig(Config):
    """Production configuration."""

    ENV = 'prod'
    DEBUG = False
    UPLOAD_FOLDER = '/Repository/python/ge.skivri.writing/backend/uploads'


class DevConfig(Config):
    """Development configuration."""

    ENV = 'dev'
    DEBUG = True
    UPLOAD_FOLDER = '/Repository/python/ge.skivri.writing/backend/uploads'
