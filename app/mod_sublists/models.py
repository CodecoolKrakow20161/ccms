from app.base_model import BaseModel
from app import db


class Sublist(BaseModel):
    __tablename__ = 'sublists'

    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text(), nullable=True)
    archived_at = db.Column(db.DateTime(), nullable=True)
