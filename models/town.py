from models.shared import db
from sqlalchemy.orm import relationship


class Town(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(500), unique=True)
	region = db.Column(db.String(500))

	def __init__(self, name, region):
		self.name = name
		self.region = region

	def __repr__(self):
		return '<Town %r>' % self.name

#Adds the town into the database 
def add_town_db(town):
	created_town = Town(name=town["name"], region=town["region"])
	db.session.add(created_town)
	db.session.commit()
	return created_town

#Gets all information about a person in the database
def get_information(id):
	town = Town.query.filter_by(id=id).first()
	if town:
		return dict_town(town)
	return None

#Gets all information about multiple people in the database based on their id's
def get_some_towns(town_ids):
	all_towns = {}
	for town_id in town_ids:
		all_towns[town_id] = get_information(town_id)
	return all_towns

#Gets information about all people in database
def get_all_towns():
	all_towns = {}
	towns = Town.query.all()
	for town in towns:
		all_towns[town.id] = dict_town(town)
	return all_towns

#Deletes a town from the db based on id
def delete_town(town_id):
	to_delete = Town.query.filter_by(id=town_id).first()
	db.session.delete(to_delete)
	db.session.commit()
	return True


#Creates a dictionary out of a Town object
def dict_town(town):
	return {'id':town.id, 'name':town.name, 'region':town.region}
