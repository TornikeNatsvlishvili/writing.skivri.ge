from flask_mail import Mail as FlaskMail, Message
from flask_cors import CORS
from backend.util import async


class Mail:
    def __init__(self):
        self.mail = FlaskMail()

    def init_app(self, app):
        self.mail.init_app(app)

    @async
    def send_notification_email(self, app):
        with app.app_context():
            msg = Message("New upload",
                    sender='writing.skivri.ge <{}>'.format(app.config['MAIL_USERNAME']),
                    recipients=[app.config['DESTINATION_EMAIL']])
            mail.send(msg)



mail = Mail()
cors = CORS()