# src/models/AccountModel.py
from marshmallow import fields, Schema
from sqlalchemy.dialects.postgresql import UUID
import datetime, uuid
from ...shared.models import db, bcrypt
from ...shared.models.BaseModel import BaseModel
from .BusinessModel import BusinessSchema

class AccountModel(BaseModel):
  """
  Account Model
  """

  # table name
  __tablename__ = 'accounts'

  name = db.Column(db.String(128), nullable=False)
  email = db.Column(db.String(128), unique=True, nullable=False)
  password = db.Column(db.String(128), nullable=False)
  phonenumber = db.Column(db.String(128), unique=True, nullable=False)
  is_active = db.Column(db.Boolean, default=True)
  is_deleted = db.Column(db.Boolean, default=False)
  deleted_on = db.Column(db.DateTime)
  businesses = db.relationship('BusinessModel', backref='accounts', lazy=True)

  # class constructor
  def __init__(self, data):
    """
    Class constructor
    """
    BaseModel.__init__(self, data)
    self.name = data.get('name')
    self.email = data.get('email')
    self.password = self.__generate_hash(data.get('password'))
    self.phonenumber = data.get('phonenumber')
    self.is_deleted = data.get('is_deleted')
    self.is_active = data.get('is_active')
    self.deleted_on = data.get('deleted_on')

  def save(self):
    db.session.add(self)
    db.session.commit()

  def update(self, data):
    for key, item in data.items():
      if key == 'password':
        self.password = self.__generate_hash(value)
      setattr(self, key, item)
    self.modified_at = datetime.datetime.utcnow()
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  @staticmethod
  def get_all_users():
    return AccountModel.query.all()

  @staticmethod
  def get_one_user(id):
    return AccountModel.query.get(id)
  
  @staticmethod
  def get_user_by_email(value):
    return AccountModel.query.filter_by(email=value).first()
  
  @staticmethod
  def get_user_by_phonenumber(value):
    return AccountModel.query.filter_by(phonenumber=value).first()

  def __generate_hash(self, password):
    return bcrypt.generate_password_hash(password, rounds=10).decode("utf-8")
  
  def check_hash(self, password):
    return bcrypt.check_password_hash(self.password, password)
  
  def __repr__(self):
    return '<Account {}>'.format(self.name)

class AccountSchema(Schema):
  id = fields.UUID(dump_only=True)
  name = fields.Str(required=True)
  email = fields.Email(required=True)
  password = fields.Str(required=True, load_only=True)
  phonenumber = fields.Str(required=True)
  is_active = fields.Boolean()
  is_deleted = fields.DateTime()
  created_at = fields.DateTime(dump_only=True)
  modified_at = fields.DateTime(dump_only=True)
  deleted_on = fields.Date()
  businesses = fields.Nested(BusinessSchema, many=True)