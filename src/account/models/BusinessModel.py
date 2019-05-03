# src/models/BusinessModel.py
from ...shared.models import db
from ...shared.models.BaseModel import BaseModel
import datetime, uuid
from sqlalchemy.dialects.postgresql import UUID
from marshmallow import fields, Schema

class BusinessModel(BaseModel):
  """
  Business Model
  """

  __tablename__ = 'businesses'

  name = db.Column(db.String(128), nullable=False)
  industry = db.Column(db.String(128), nullable=False)
  description = db.Column(db.Text, nullable=False)
  owner_id = db.Column(UUID(as_uuid=True), db.ForeignKey('accounts.id'), nullable=False)

  def __init__(self, data):
    BaseModel.__init__(self, data)
    self.name = data.get('name')
    self.industry = data.get('industry')
    self.description = data.get('description')
    self.owner_id = data.get('owner_id')

  def save(self):
    db.session.add(self)
    db.session.commit()

  def update(self, data):
    for key, item in data.items():
      setattr(self, key, item)
    self.modified_at = datetime.datetime.utcnow()
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()
  
  @staticmethod
  def get_all_businesses():
    return BusinessModel.query.all()
  
  @staticmethod
  def get_one_business(id):
    return BusinessModel.query.get(id)

  def __repr__(self):
    return '<id {}>'.format(self.id)

class BusinessSchema(Schema):
  """
  Business Schema
  """
  id = fields.UUID(dump_only=True)
  name = fields.Str(required=True)
  industry = fields.Str(required=True)
  description = fields.Str(required=True)
  owner_id = fields.UUID(required=True)
  created_at = fields.DateTime(dump_only=True)
  modified_at = fields.DateTime(dump_only=True)