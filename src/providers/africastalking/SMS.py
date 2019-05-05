from marshmallow import fields, Schema
import requests, json
from ...config import CustomConfigs
from .AfricasTalkingService import AfricasTalkingService
from ...services.RestService import  RestClient, RestRequest

class SMSModel:
    def __init__(self,data):
        self.username = data.get('username')
        self.to = data.get('to')
        self.message = data.get('message')
        self.bulkSMSMode = data.get('bulkSMSMode')
        self.enqueue = data.get('enqueue')
        self.retryDurationInHours = data.get('retryDurationInHours')
   
def send_sms(to, message):
    sms_body = {
        "username":CustomConfigs.AFRICASTALKING_PRODUCTION_USERNAME,
        "to":to,
        "message":message,
        "bulkSMSMode": 1,
        "enqueue": 1,
        "retryDurationInHours":1
    }
    response = AfricasTalkingService().send_sms(sms_body)
    return response

class SMSRequestSchema(Schema):
    username = fields.Str(required=True)
    to = fields.Str(required=True)
    message = fields.Str(required=True)
    bulkSMSMode = fields.Int()
    enqueue = fields.Int()
    retryDurationInHours = fields.Int()

class RecipientSchema(Schema):
    StatusCode = fields.Int()
    number = fields.Str()
    status = fields.Str()
    cost = fields.Str()
    messageId = fields.Str()
    
class SMSMessageDataSchema(Schema):
    Message = fields.Str()
    Recipients = fields.Nested(RecipientSchema, many=True)

class SMSResponseSchema(Schema):
    SMSMessageData = fields.Nested(SMSMessageDataSchema)

