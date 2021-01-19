from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField

from wtforms.validators import input_required, Length

class LoginForm(FlaskForm):
    username = StringField('username', validators=[input_required(), Length(min=2,max=10)])
    password = PasswordField('username', validators=[input_required()])
    submit = SubmitField()