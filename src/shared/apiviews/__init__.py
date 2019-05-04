from flask import jsonify

def custom_response(data, status_code):
    """
    Custom Response Function
    """
    return jsonify(data), status_code