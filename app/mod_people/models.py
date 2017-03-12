from app.base_model import BaseModel
from app import db


class Person(BaseModel):
    __tablename__ = 'people'

    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(255), nullable=False, name="e-mail")
    phone = db.Column(db.String(30), nullable=False)

    def full_name(self):
        """
        :return: Full name of person (first and last name)
        """
        return "{} {}".format(self.first_name, self.last_name)
