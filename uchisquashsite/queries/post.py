from tkinter import image_names
from uchisquashsite.models import Post
from uchisquashsite.models import db

def new_post(img_url, body, title, dt):
    post = Post(image_url=img_url, body=body,
                title=title, date=dt)
    db.session.add(post)
    db.session.commit()

def remove_post(pid):
    post = Post.query.filter_by(id=pid).first()
    db.session.delete(post)