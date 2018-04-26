from flask import Blueprint, request, jsonify
from models import person, town

interact = Blueprint('interact', __name__, url_prefix='/interact')
400_RESPONSE = ('', 400)
200_RESPONSE = ('', 200)

#### People Endpoints ####

#Adds a person into the database
@interact.route('/add_person', methods=['POST'])
def add_person():
	if request.is_json:
		person_json = request.get_json()
		if person.add_person_db(person_json):
			return 200_RESPONSE
	return 400_RESPONSE

#Using an ID, provide information about a person
@interact.route('/display_person/<person_id>', methods=['GET'])
def display_person(person_id):
	person_info = person.get_information(person_id)
	if person_info:
		return jsonify(person_info)
	return 400_RESPONSE

#Using an ID, provide information about either all people or a subset based on person id
@interact.route('/display_people', methods=['GET', 'POST'])
def display_people():
	people_info = None
	if request.method == 'GET':
		people_info = person.get_all_people()
	elif request.method == 'POST':
		if request.is_json:
			people_info = person.get_some_people(request.get_json())
	if people_info:
		return jsonify(people_info)
	return 400_RESPONSE

@interact.route('/delete_person/<person_id>', methods=['DELETE'])
def delete_person(person_id):
	return 400_RESPONSE


#### Town Endpoints ####

#Using an ID, provide information about a town
@interact.route('/display_town/<town_id>', methods=['GET'])
def display_town(town_id):
	town_info = town.get_information(town_id)
	if town_info:
		return jsonify(town_info)
	return 400_RESPONSE

#Adds a town into the database
@interact.route('/add_town', methods=['POST'])
def add_town():
	if request.is_json:
		town_json = request.get_json()
		print(town_json)
		if town.add_town_db(town_json):
			return 200_RESPONSE
	return 400_RESPONSE