from marshmallow import fields, Schema
from ....shared.models import db
from ....providers.africastalking.SMS import send_sms


class SMSModel():
    
    def __init__(self, data):
        self.to = data.get('to')
        self.message = data.get('message')
    
    def send(self):
        return send_sms(self.to, self.message)

class SMSSchema(Schema):
    to = fields.Str(required=True)
    message = fields.Str(required=True)