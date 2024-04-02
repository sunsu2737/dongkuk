from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length
class CheckForm(FlaskForm):
    name = StringField("이름", validators=[Length(min=2)])