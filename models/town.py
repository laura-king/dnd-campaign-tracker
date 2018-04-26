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
	db.session.add(Town(name=town['name'], region=town['region']))
	db.session.commit()
	return True

#Gets all information about a person in the database
def get_information(id):
	town = Town.query.filter_by(id=id).first()
	if town:
		return {'name':town.name, 'region':town.region}
	return None

