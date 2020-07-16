# Imports

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Models.

class Todo(db.Model):
	__tablename__ = 'todos'
	id = db.Column(db.Integer, primary_key=True)
	description = db.Column(db.String(), nullable=False)
	completed = db.Column(db.Boolean, default=False)