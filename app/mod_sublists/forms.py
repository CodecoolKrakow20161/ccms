from wtforms_alchemy import ModelForm
from wtforms.fields import StringField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, Regexp
from wtforms_alchemy.validators import Unique
from app.mod_sublists.models import Sublist


class SublistForm(ModelForm):
    class Meta:
        model = Sublist
        strip_string_fields = True

    name = StringField(
        validators=[DataRequired(), Length(min=3, max=100)]
    )

    description = TextAreaField()
