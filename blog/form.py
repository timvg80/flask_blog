from flask_wtf import FlaskForm
from wtforms import StringField, validators
from author.form import RegisterForm


class SetupForm(RegisterForm):
    name = StringField('Blog name', [
        validators.DataRequired(),
        validators.Length(max=80)
    ])