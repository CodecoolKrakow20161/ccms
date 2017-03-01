from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class KlassForm(FlaskForm):
    name = StringField('Class name', [
        DataRequired(message='Plase give a class name')
    ])