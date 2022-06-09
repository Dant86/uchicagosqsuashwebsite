from flask import Blueprint, render_template
from requests import get
from uchisquashsite.queries.player import get_active_roster

base = Blueprint('base', __name__)

CHRIS_URL = 'https://api.ussquash.com/resources/res/user/204905/rankings'

@base.route('/')
def homepage():
    return render_template('index.html')

@base.route('/about')
def about():
    return render_template('about.html')

@base.route('/roster')
def roster():
    roster_sorted = sorted(get_active_roster(), key=lambda x: x[2])
    roster = [(p, f'{r:.2f}', x) for p, r, x in roster_sorted]
    l = len(roster)
    chris_rating = get(CHRIS_URL).json()[0]['Rating']
    return render_template('roster.html', roster=roster, l=l, chris_rating=chris_rating)