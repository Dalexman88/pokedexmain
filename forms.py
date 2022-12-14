from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class searchpokemonform(FlaskForm):
  name=StringField('Pokemon name')
  submit=SubmitField()


class UserLoginForm(FlaskForm):
  email = StringField('Email', validators = [DataRequired(), Email()])
  password = PasswordField('Password', validators = [DataRequired()])
  submit_button = SubmitField()