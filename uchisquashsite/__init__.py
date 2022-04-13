from flask import Flask
from dotenv import load_dotenv
from os import getenv

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
        db.create_all()
        db.session.commit()
        return app
