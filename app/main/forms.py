from flask_wtf import FlaskForm
from wtforms.widgets import TextArea
from wtforms.validators import InputRequired
from wtforms import SelectField,StringField,TextAreaField,SubmitField

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [InputRequired()])
    submit = SubmitField('Submit')

class Pitches(FlaskForm):
   message = StringField('comment', widget=TextArea(), validators=[InputRequired()])
   category = SelectField('Pitch Category',choices=[('Football','Football'),('Basketball','NBA/Golden State Warriors'),('Tennis','Tennis/BestPlayers'),('Hockey','Hockey/Games')])
class Comments(FlaskForm):
      comment = StringField('comment', widget=TextArea(), validators=[InputRequired()])
