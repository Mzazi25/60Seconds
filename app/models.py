from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    password_hash = db.Column(db.String(255))
    # liked = db.relationship('Review',backref = 'user',lazy = "dynamic")

    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)


    def __repr__(self):
        return f'User {self.username}'

class Pitch (db.Model):
    __tablename__= "pitchs"
    """ 
    Added class for Pitches
    """

    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    message = db.Column(db.String(), unique=False,nullable=False)
    category = db.Column(db.String(20),nullable=False)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow(), nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id') )
    likes = db.relationship('PostLike', backref='pitchs', lazy='dynamic')

class PostLike(db.Model):
    __tablename__= 'post_like'
    
    id = db.Column(db.Integer, primary_key=True)
    users_id = db.Column(db.Integer,db.ForeignKey('users.id') )
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitchs.id') )
    comment = db.Column(db.String(), unique=False, nullable=False)
    created = db.Column(db.DateTime(), default=datetime.utcnow(), nullable=False)

