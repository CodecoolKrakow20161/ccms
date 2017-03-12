from app.base_model import BaseModel
from app import db


class Person(BaseModel):
    __tablename__ = 'people'

    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(255), nullable=False, name="e-mail")
    phone = db.Column(db.String(30), nullable=False)
