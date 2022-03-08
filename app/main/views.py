from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import Pitches, Comments
from ..models import User
from flask_login import login_required,current_user
from .. import db,login_manager

# creating an auth instance
@login_manager.user_loader
def load_user(user_id):
        return User.query.get(int(user_id))

login_manager.login_view = 'main.login'


#views
@main.route('/')
def index():
    '''
    view root page function that returns indext.html and its data
    '''
    return render_template('index.html')