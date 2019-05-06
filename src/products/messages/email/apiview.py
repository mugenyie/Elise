from flask import request, json, Response, Blueprint, g, jsonify
from ....shared.apiviews import custom_response
from .model import EmailModel, EmailSchema


email_api = Blueprint('email_api', __name__)
email_schema = EmailSchema()

@email_api.route('/', methods=['POST'])
def send():
    """Send Email from elise api"""
    req_data = request.get_json()
    data, error = email_schema.load(req_data)

    if error:
        return custom_response(error, 400)

    email = EmailModel(data)
    response = email.send()
    return custom_response(response.body, response.status_code)