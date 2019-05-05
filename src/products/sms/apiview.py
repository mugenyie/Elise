from flask import request, json, Response, Blueprint, g, jsonify
from xml.etree import ElementTree
from ...shared.apiviews import custom_response
from .model import SMSModel, SMSSchema
from ...providers.africastalking.SMS import send_sms
from ...providers.africastalking.AfricasTalkingService import AfricasTalkingService


sms_api = Blueprint('sms_api', __name__)
sms_schema = SMSSchema()

@sms_api.route('/', methods=['POST'])
def send():
    """Send sms from elise api"""
    req_data = request.get_json()
    data, error = sms_schema.load(req_data)

    if error:
        return custom_response(error, 400)

    sms = SMSModel(data)
    response = sms.send()
    return custom_response(ElementTree.tostring(response.text), response.status_code)