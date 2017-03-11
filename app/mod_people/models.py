from app.base_model import BaseModel
from app import db


class People(BaseModel):
    __tablename__ = 'people'

    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, name="e-mail")
    phone = db.Column(db.String, nullable=False)
