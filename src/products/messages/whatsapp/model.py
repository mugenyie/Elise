from marshmallow import fields, Schema
from ....shared.models import db
from ....providers.twilio.TwilioService import TwilioService

class WhatsappModel():
    
    def __init__(self, data):
        self.to = data.get('to')
        self.message = data.get('message')
    
    def send(self):
        return TwilioService().send_whatsapp(self.to, self.message)

class WhatsappSchema(Schema):
    to = fields.Str(required=True)
    message = fields.Str(required=True)