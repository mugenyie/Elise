from sqlalchemy.dialects.postgresql import UUID
import datetime, uuid
from . import db


class BaseModel(db.Model):

    """Base Model"""
    __abstract__ = True

    id = db.Column(UUID(as_uuid=True), unique=True, nullable=False, primary_key=True, default=uuid.uuid4())
    created_on = db.Column(db.DateTime)
    modified_on = db.Column(db.DateTime)

    def __init__(self, data):
        self.created_on = datetime.datetime.utcnow()
        self.modified_on= datetime.datetime.utcnow()