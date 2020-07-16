#Importing Flask so that I can use the helpful framework
from flask import Flask, render_template
#Importing Flack SQLAlchemy so I can use these commands in code ex. db.session.X
from flask_sqlalchemy import SQLAlchemy

#assigning the name of my app to "app" so as to run the app via this variable
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html', data=[{
		'description': 'Stuff'
	}, {
		'description': 'Things'
	}, {
		'description': 'WOW Take my Accounts'
	}])