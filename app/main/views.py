from flask import render_template,request,redirect,url_for,abort
from . import main
from flask.helpers import flash, url_for
from flask_wtf import Form
from wtforms import BooleanField, PasswordField, TextAreaField, validators

from .forms import UpdateProfile,Pitches,Comments
from ..models import User, Pitch, PostLike
from flask_login import login_required,current_user
from .. import db,login_manager,photos

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

@main.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    
    # fetch data
    pitch = Pitch.query.all()
    user = User.query.all()
    form = Pitches()

    if form.validate_on_submit():
        category = form.category.data
        message = form.message.data

        pitch = Pitch(category=category, message=message,user_id=current_user.id)

        # add data to db
        db.session.add(pitch)
        db.session.commit()
        return redirect(url_for('.profile'))
    return render_template("profile/profile.html", user = user,pitch=pitch,form=form)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():

        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))