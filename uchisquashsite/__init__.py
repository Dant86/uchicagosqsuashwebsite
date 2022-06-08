from flask import Flask
from dotenv import load_dotenv
from os import getenv
from pandas import read_csv
from uchisquashsite.queries.player import create_player

def player_from_row(row):
    fname = str(row['fname'])
    minitial = str(row['minitial'])
    lname = str(row['lname'])
    yr = int(row['Grad'])
    bio = str(row['Bio'])
    email = str(row['Email'])
    major = str(row['Major'])
    purl = str(row['Photo_URL'])
    create_player(fname, lname, minitial, yr, major, email, bio, purl)

def create_app(testing=True):
    '''
    Create an instance of the Flask application.
    '''
    app = Flask(__name__)
    
    # Load config from .env file
    load_dotenv()
    ks = ['SECRET_KEY', 'APP', 'FLASK_ENV']
    db_ext = '_TEST' if testing else ''
    db_uri = f'SQLALCHEMY{db_ext}_DATABASE_URI'
    ks.append(db_uri)
    for k in ks:
        if k == 'SQLALCHEMY_TEST_DATABASE_URI':
            app.config['SQLALCHEMY_DATABASE_URI'] = getenv(k)
        else:
            app.config[k] = getenv(k)

    # load models
    from uchisquashsite.models import db
    from uchisquashsite.models import Player, Match, Post, Practice
    db.init_app(app)

    # load blueprints
    from uchisquashsite.routes.base import base
    app.register_blueprint(base)
    with app.app_context():
        if testing:
            Player.__table__.drop(db.engine)
        db.session.commit()
        db.create_all()
        db.session.commit()
        try:
            df = read_csv('playerdata.csv')
            df['Photo_URL'] = df['Photo_URL'].fillna('')
            df['minitial'] = df['minitial'].fillna('')
            df.apply(player_from_row, axis=1)
        except Exception as e:
            print(e)
        return app
