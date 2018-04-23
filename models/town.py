from models.shared import db
from sqlalchemy.orm import relationship


class Town(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(500), unique=True)
	region = db.Column(db.String(500))

	def __init__(self, name, town, status):
		self.name = name
		self.region = region

	def __repr__(self):
		return '<Town %r>' % self.name
