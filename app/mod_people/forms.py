from wtforms_alchemy import ModelForm
from app.mod_people.models import Person


class PersonForm(ModelForm):
    class Meta:
        model = Person
        strip_string_fields = True