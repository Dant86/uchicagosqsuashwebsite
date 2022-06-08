from uchisquashsite.models import Player
from uchisquashsite.models import db
from requests import get
from pandas import DataFrame

USSQUASH_API_URL = 'https://api.ussquash.com/resources/teams/29927/players'

def get_player(id_):
    return Player.query.filter_by(id=id_).first()

def create_player(fname, lname, minitial,
                  year, major, email, bio='', photo_url='', pos=''):
    photo_url = 'static/images/editedlogo.png' if photo_url == '' else photo_url
    p = Player(fname=fname, lname=lname, minitial=minitial,
               photo_url=photo_url, graduation_year=year, graduated=False,
               bio=bio, position=pos, email=email, major=major)
    db.session.add(p)
    db.session.commit()

def set_photo_url(p, url):
    p.url = url
    db.session.commit()

def graduate(p):
    p.graduated = True
    db.session.commit()

def add_position(p, pos):
    p.position = pos
    db.session.commit()

def get_active_roster():
    r = get(USSQUASH_API_URL)
    df = DataFrame(r.json())[['player', 'CurrentRating', 'TeamPosition']]
    active_players = Player.query.filter_by(graduated=False).all()
    results = []
    for player in active_players:
        query_string = f'{player.lname}, {player.fname} {player.minitial}'
        if df[df['player'] == query_string].empty:
            query_string += '.'
        rating = float(df[df['player'] == query_string]['CurrentRating'])
        position = int(df[df['player'] == query_string]['TeamPosition'])
        results.append((player, rating, position))
    return results
