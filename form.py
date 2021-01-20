from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField, FileField, TextAreaField

from wtforms.validators import input_required, Length

class LoginForm(FlaskForm):
    username = StringField('username', validators=[input_required(), Length(min=2,max=10)])
    password = PasswordField('password', validators=[input_required()])
    submit = SubmitField()

class destination_form(FlaskForm):
    name = StringField('name', validators=[input_required()])
    address = TextAreaField('address', validators=[input_required()])
    description = TextAreaField('description', validators=[input_required()])
    # picture = FileField('picture')
    submit = SubmitField()