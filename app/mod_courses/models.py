from app.base_model import BaseModel
from app import db


class Course(BaseModel):
    __tablename__ = 'courses'

    name = db.Column(db.String, nullable=False, unique=True)
