from wtforms_alchemy import ModelForm
from app.mod_classes.models import Klass


class KlassForm(ModelForm):
    class Meta:
        model = Klass
        strip_string_fields = True