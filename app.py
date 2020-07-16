#Importing Flask so that I can use the helpful framework
from flask import Flask, render_template
#Helper for migrating in flask command line style
from flask_migrate import Migrate
from models import *
from config import Config


APPLICATION_NAME = "app.py"

#assigning the name of my app to "app" so as to run the app via this variable
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app) 
migrate = Migrate(app, db)

# Set the Config file 

class Todo(db.Model):
	__tablename__ = 'todos'
	id = db.Column(db.Integer, primary_key=True)
	description = db.Column(db.String(), nullable=False)
	completed = db.Column(db.Boolean, default=False)


@app.route('/')
def index():
	return render_template('index.html', data=Todo.query.order_by('id').all())




