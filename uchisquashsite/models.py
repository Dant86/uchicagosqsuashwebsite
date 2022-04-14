from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Player(db.Model):

    __tablename__ = 'player'

    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(255))
    lname = db.Column(db.String(255))
    minitial = db.Column(db.String(1), default='')
    ladder_pos = db.Column(db.Integer)
    photo_url = db.Column(db.String(255), default='')
    graduation_year = db.Column(db.Integer)
    graduated = db.Column(db.Boolean, default=False)
    bio = db.Column(db.Text, default='')
    position = db.Column(db.String(255), default='')
    email = db.Column(db.String(255))
    major = db.Column(db.String(255))

class Match(db.Model):

    __tablename__ = 'match'

    id = db.Column(db.Integer, primary_key=True)
    home = db.Column(db.Boolean)
    opponent = db.Column(db.String(255))
    date = db.Column(db.DateTime)
    our_score = db.Column(db.Integer, default=0)
    their_score = db.Column(db.Integer, default=0)
    happened = db.Column(db.Boolean, default=False)

class Post(db.Model):

    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(255))
    body = db.Column(db.Text)
    title = db.Column(db.String(255))
    date = db.Column(db.DateTime)

class Practice(db.Model):

    __tablename__ = 'practice'

    id = db.Column(db.Integer, primary_key=True)
    dt = db.Column(db.DateTime)
    cancelled = db.Column(db.Boolean, default=False)
