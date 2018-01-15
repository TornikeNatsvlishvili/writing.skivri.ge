from flask import Blueprint
from .views.upload import Upload

api = Blueprint('api', __name__, url_prefix='/api/v1')

api.add_url_rule('/upload', view_func=Upload.as_view('upload'))
