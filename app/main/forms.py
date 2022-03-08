from flask_wtf import FlaskForm
from wtforms.widgets import TextArea
from wtforms.validators import InputRequired
from wtforms import SelectField,StringField


class Pitches(FlaskForm):
   message = StringField('message', widget=TextArea(), validators=[InputRequired()])
   category = SelectField('Pitch Category',choices=[('Love','Love'),('Positive','Positive/Inspiring'),('Meme','Memes/Funny'),('Family','Family/Life')])
class Comments(FlaskForm):
      comment = StringField('comment', widget=TextArea(), validators=[InputRequired()])
