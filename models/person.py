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
