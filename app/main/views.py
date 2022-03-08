from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import Pitches, Comments
from ..models import User, Pitch, PostLike
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

@main.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    likes = PostLike.query.all()
    form = Comments()
    if form.validate_on_submit():
        new_comment = PostLike(comment=form.comment.data,users_id=current_user.id)
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('main.dashboard'))
    pitch = Pitch.query.all()
    user = User.query.all()
    return render_template('dashboard.html',likes=likes, user=user, form=form,pitch=pitch)

@main.route('/user/<uname>')

def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)