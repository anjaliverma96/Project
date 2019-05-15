#IMPORT FLASK
from flask import Flask, jsonify

#FOR BACKEND SQL DATABASE CONNECTION
from flask_sqlalchemy import SQLAlchemy

#FOR ERROR LOGGING
from logging import FileHandler, WARNING

#FOR CSRF PROTECTION WHILE SUBMITTING FORMS

app = Flask(__name__)
# set the configuration

SECRET_KEY = 'hardtoguesskey'

DATABASE_USERNAME = 'YourDatabaseuserName'
DATABASE_PASSWORD = 'YourDatabasePassword'
DATABASE_NAME = 'YourDatabaseName'
DATABASE_ADDRESS = 'YourDatabaseAddress(either ip or url address)'
DATABASE_URI = 'mysql+pymysql://%s:%s@%s/%s?use_unicode=1&charset=utf8' % (DATABASE_USERNAME,DATABASE_PASSWORD,DATABASE_ADDRESS,DATABASE_NAME)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI

#create the db instance of SQLAlchemy
db = SQLAlchemy(app)

class Jokes(db.Model):
    __tablename__ = "joketable"

    id = db.Column(db.Integer, primary_key=True)
    jokes = db.Column(String(1000))

class Ratings(db.Model):

    __tablename__ = "ratings"

    id = db.Column(db.Integer, primary_key=True)
    joke_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    rating = db.Column(db.Integer)

db.create_all()

#ERROR LOGGIN
#LOGS ERROR TOO THE FILE CALLED - errorlog.txt
file_handler = FileHandler('errorlog.txt')
file_handler.setLevel(WARNING)
app.logger.addHandler(file_handler)

#SET SECRET KEY
app.secret_key = "some_strong_secret_key"

#IMPORT VIEWS WHICH IS THE CONTROLLER IN THE MVC
import views