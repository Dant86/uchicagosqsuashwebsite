from uchisquashsite.models import Player
from uchisquashsite.models import db
from requests import get
from pandas import DataFrame

USSQUASH_API_URL = 'https://api.ussquash.com/resources/teams/29927/players'

def get_player(id_):
    return Player.query.filter_by(id=id_).first()

def create_player(fname, lname, rating, ladder_pos,
                  year, major, email, bio='', photo_url='', pos=''):
    p = Player(fname, lname, rating, ladder_pos, photo_url,
               year, bio, pos, email, major)
    db.session.add(p)
    db.session.commit()

def challenge_match(pw, pl):
    r1 = pw.ladder_pos
    r2 = pl.ladder_pos
    pw.ladder_pos = max(r1, r2)
    pl.lader_pos = min(r1, r2)
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

def get_player_ratings():
    r = get(USSQUASH_API_URL)
    df = DataFrame(r.json())[['player', 'CurrentRating']]
    active_players = Player.query.filter_by(graduated=False).all()
    results = []
    for player in active_players:
        query_string = f'{player.lname}, {player.fname} {player.minitial}'
        rating = float(df[df['player'] == query_string]['CurrentRating'])
        results.append((player, rating))
    return results
