from app.base_model import BaseModel
from app import db

class Class(BaseModel):
    __tablename__ = 'classes'

    name = db.Column(db.String, nullable=False)