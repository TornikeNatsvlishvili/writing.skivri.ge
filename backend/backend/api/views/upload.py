from flask import request, current_app, jsonify
from flask.views import MethodView
from werkzeug.utils import secure_filename
from backend.extensions import mail
import os


ALLOWED_EXTENSIONS = set(['pdf', 'png', 'jpg', 'jpeg', 'gif'])

class Upload(MethodView):
    def post(self):
        # check if the post request has the file part
        if 'file' not in request.files:
            return jsonify({"error": "Missing attached file key"}), 400

        file = request.files['file']
        # if user does not select files, browser will
        # submit a empty part without filename
        if file.filename == '':
            return jsonify({"error": "Selected file has no name"}), 400

        if file and Upload.allowed_file(file.filename):
            filename = secure_filename(file.filename)
            addition = 0
            new_name = filename
            while os.path.exists(os.path.join(current_app.config['UPLOAD_FOLDER'], new_name)):
                new_name = '{}_{}'.format(filename, addition)
                addition += 1
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], new_name))

            mail.send_notification_email(current_app._get_current_object())

            return jsonify({"success": True})

        return jsonify({"success": False})

    @staticmethod
    def allowed_file(filename):
        return '.' in filename and \
            filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS