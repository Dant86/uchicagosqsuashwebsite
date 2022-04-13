from uchisquashsite.models import Practice
from uchisquashsite.models import db

def new_practice(date):
    p = Practice(dt=date)
    db.session.add(p)
    db.session.commit()

def cancel_practice(pid):
    p = Practice.query.filter_by(id=pid).first()
    db.session.remove(p)
    db.session.commit()