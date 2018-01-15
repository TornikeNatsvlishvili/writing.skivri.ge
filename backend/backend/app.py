from flask import Flask, jsonify
from backend.settings import ProdConfig
from backend.api import api
from backend.extensions import mail, cors


def create_app(config_object=ProdConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    return app


def register_blueprints(app):
    app.register_blueprint(api)
    return None


def register_extensions(app):
    mail.init_app(app)
    cors.init_app(app)
    return None
