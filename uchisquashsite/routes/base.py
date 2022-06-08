from flask import Blueprint, render_template, jsonify
from uchisquashsite.queries.player import get_active_roster

base = Blueprint('base', __name__)

@base.route('/')
def homepage():
    return render_template('index.html')

@base.route('/about')
def about():
    return render_template('about.html')

@base.route('/roster')
def roster():
    print(get_active_roster())
    return jsonify(success=True)