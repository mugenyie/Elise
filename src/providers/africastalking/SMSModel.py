from marshmallow import fields, Schema
import requests, json

class SMSModel:
    def __init__(self,data):
        self.username = data.get('username')
        self.to = data.get('to')
        self.message = data.get('message')
        self.from_ = data.get('from')
        self.bulkSMSMode = data.get('bulkSMSMode')
        self.enqueue = data.get('enqueue')
        self.keyword = data.get('keyword')
        self.linkId = data.get('linkId')
        self.retryDurationInHours = data.get('retryDurationInHours')

    def send_sms(self):
        response = requests.post('https://api.sandbox.africastalking.com/version1/messaging',json=json.dumps(self))
        json_data = response.get_json()
        return json.load(json_data)
        # return SMSResponseSchema().load(json_data)


class SMSRequestSchema(Schema):
    username = fields.Str(required=True)
    to = fields.Str(required=True)
    message = fields.Str(required=True)
    from_ = fields.Str() #SenderId
    bulkSMSMode = fields.Int()
    enqueue = fields.Int()
    keyword = fields.Str()
    linkId = fields.Str()
    retryDurationInHours = fields.Int()

# class SMSResponseSchema(Schema):
#     SMSMessageData = fields.Nested(SMSMessageDataSchema)

# class SMSMessageDataSchema(Schema):
#     Message = fields.Str()
#     Recipients = fields.Nested(RecipientSchema, many=True)

# class RecipientSchema(Schema):
#     StatusCode = fields.Int()
#     number = fields.Str()
#     status = fields.Str()
#     cost = fields.Str()
#     messageId = fields.Str()