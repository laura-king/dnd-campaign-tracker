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
	all_people = {}
	for person_id in people_ids:
		all_people[person_id] = get_information(person_id)
	return all_people

#Gets information about all people in database
def get_all_people():
	all_people = {}
	people = Person.query.all()
	for person in people:
		all_people[person.id] = dict_person(person)
	return all_people

#Gets all townspeople based on a town id
def get_townspeople(town_id):
	all_people = {}
	people = Person.query.filter_by(town=town_id).all()
	for person in people:
		all_people[person.id] = dict_person(person)
	return all_people

#Deletes a person from the db based on id
def delete_person(person_id):
	to_delete = Person.query.filter_by(id=person_id).first()
	db.session.delete(to_delete)
	db.session.commit()
	return True

###  Helper Functions  ###

#Creates a dictionary out of a Person object
def dict_person(person):
	return {'id':person.id, 'name':person.name, 'town':person.town, 'status':person.status}
