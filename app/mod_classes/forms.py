from app.base_form import BaseForm
from wtforms import StringField
from wtforms.validators import DataRequired

class KlassForm(BaseForm):
    name = StringField('Class name', [
        DataRequired(message='Plase give a class name')
    ])