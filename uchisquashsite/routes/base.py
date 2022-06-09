from flask import Blueprint, render_template, jsonify
from requests import get
from pandas import DataFrame, to_datetime
from uchisquashsite.queries.player import get_active_roster
from uchisquashsite.queries.match import get_all_matches

base = Blueprint('base', __name__)

CHRIS_URL = 'https://api.ussquash.com/resources/res/user/204905/rankings'
STANDINGS_URL = 'https://api.ussquash.com/resources/divisions/standings/3482'

@base.route('/')
def homepage():
    return render_template('index.html')

@base.route('/about')
def about():
    r = get(STANDINGS_URL)
    df = DataFrame(r.json())
    rank = int(df[df['teamid'] == 29927]['hGroup'])
    return render_template('about.html', rank=rank)

@base.route('/roster')
def roster():
    roster_sorted = sorted(get_active_roster(), key=lambda x: x[2])
    roster = [(p, f'{r:.2f}', x) for p, r, x in roster_sorted]
    l = len(roster)
    chris_rating = get(CHRIS_URL).json()[0]['Rating']
    return render_template('roster.html', roster=roster, l=l,
                           chris_rating=chris_rating)

@base.route('/matches')
def matches():
    ms = get_all_matches()
    ms['date'] = to_datetime(ms['date'])
    ms = ms.sort_values('date')
    ms['date'] = ms['date'].dt.strftime('%A, %B %d, %Y')
    return render_template('matches.html', ms=ms)