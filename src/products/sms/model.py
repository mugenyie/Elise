from shared.models import db
from marshmallow import fields, Schema
from shared.models.BaseModel import BaseModel


class SMSModel(BaseModel):
    
    def __init__(self, data):

class SMSSchema(Schema):