from app.base_model import BaseModel
from app import db

class Klass(BaseModel):
    __tablename__ = 'classes'

    name = db.Column(db.String, nullable=False, unique=True)