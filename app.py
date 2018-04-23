'''
Handles the starting process for the database and the models
'''
from flask import Flask, render_template, request
from models.shared import db
from models import person, town


#start and configure app
app = Flask(__name__)
app.config.from_pyfile('app.cfg')
db.init_app(app)

@app.route('/')
def starter_page():
	'''
	Default starter page
	'''
	return 'we here'


if __name__ == "__main__":
	app.run()

