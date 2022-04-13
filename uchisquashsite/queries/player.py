from uchisquashsite.models import Player
from uchisquashsite.models import db

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
