from wtforms_alchemy import ModelForm
from app.mod_courses.models import Course


class CourseForm(ModelForm):
    class Meta:
        model = Course
        strip_string_fields = True
        field_args = {
            "name": {
                "filters": [
                    lambda s: s.upper() if s else s
                ]
            }
        }