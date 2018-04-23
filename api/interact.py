from flask import Blueprint, request, jsonify
from models.person import add_person_db
from models.town import add_town_db

interact = Blueprint('interact', __name__, url_prefix='/interact')

#Adds a person into the database
@interact.route('/add_person', methods=['POST'])
def add_person():
	if request.is_json:
		person_json = request.get_json()
		if add_person_db(person_json):
			return '', 200
	return '', 400


#Adds a town into the database
@interact.route('/add_town', methods=['POST'])
def add_town():
	if request.is_json:
		town_json = request.get_json()
		print(town_json)
		if add_town_db(town_json):
			return '', 200
	return '', 400