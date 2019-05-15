from flask_app import db, app
import String


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