from flask import request, json, Response, Blueprint, g, jsonify
from ....shared.apiviews import custom_response
from .model import WhatsappModel, WhatsappSchema


whatsapp_api = Blueprint('whatsapp_api', __name__)
whatsapp_schema = WhatsappSchema()

@whatsapp_api.route('/', methods=['POST'])
def send():
    """Send whatsapp from elise api"""
    req_data = request.get_json()
    data, error = whatsapp_schema.load(req_data)

    if error:
        return custom_response(error, 400)

    whatsapp = WhatsappModel(data)
    response = whatsapp.send()
    return custom_response(response.sid, 202)