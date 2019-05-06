from marshmallow import fields, Schema
from ....shared.models import db
from ....providers.sendgrid.SendgridService import send_mail


class EmailModel:
    
    def __init__(self, data):
        self.from_ = data.get('from_')
        self.to = data.get('to')
        self.subject = data.get('subject')
        self.html_message = data.get('message')
    
    def send(self):
        return send_mail(self.from_,self.to,self.subject,self.html_message)

class EmailSchema(Schema):
    from_ = fields.Str(required=True)
    to = fields.Str(required=True)
    subject = fields.Str(required=True)
    html_message = fields.Str(required=True)