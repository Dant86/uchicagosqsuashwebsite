from flask import Blueprint, render_template

base = Blueprint('base', __name__)

@base.route('/')
def homepage():
    return render_template('index.html')

@base.route('/about')
def about():
    return render_template('about.html')