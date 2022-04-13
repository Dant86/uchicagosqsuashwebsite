from uchisquashsite.models import Match
from uchisquashsite.models import db

def new_match(home, opp, date):
    match = Match(home=home, opponent=opp, date=date)
    db.session.add(match)
    db.session.commit()

def log_match_scores(mid, our_s, their_s):
    match = Match.query.filter_by(id=mid)
    match.our_score = our_s
    match.their_score = their_s
    match.happened = True
    db.session.commit()