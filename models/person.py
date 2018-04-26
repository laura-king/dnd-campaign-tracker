from models.shared import db
from sqlalchemy.orm import relationship


class Person(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(500))
	town = db.Column(db.Integer, db.ForeignKey('town.id'))
	status = db.Column(db.String(500), default='alive')

	def __init__(self, name, town, status):
		self.name = name
		self.town = town
		self.status = status

	def __repr__(self):
		return '<Person %r>' % self.name

#Adds the person into the database
def add_person_db(person):
	db.session.add(Person(name=person['name'], town=person['town'], status=person['status']))
	db.session.commit()
	return True

#Gets all information about one person in the database
def get_information(id):
	person = Person.query.filter_by(id=id).first()
	if person:
		return dict_person(person)
	return None

#Gets all information about multiple people in the database based on their id's
def get_some_people(people_ids):
	all_people = []
	for person_id in people_ids:
		person_info = get_information(person_id)
		if person_info:
			all_people.append(person_info)
	return {'people' : all_people}

#Gets information about all people in database
def get_all_people():
	all_people = []
	people = Person.query.all()
	for person in people:
		all_people.append(dict_person(person))
	return {'people' : all_people}

#Creates a dictionary out of a Person object
def dict_person(person):
	return {'name':person.name, 'town':person.town, 'status':person.status}
