from flask import Flask
from flask_testing import LiveServerTestCase
from flask_sqlalchemy import SQLAlchemy

class APITest(LiveServerTestCase):
    def __init__(self):
        super().__init__()
        self.db = SQLAlchemy()

    def create_app(self):

        app = Flask(__name__)
        app.config.from_pyfile('test_app.cfg')
        db.init_app(app)

        return app

    def setUp(self):

        db.create_all()

    def tearDown(self):

        db.session.remove()
        db.drop_all()
