from flask import json, Response

def custom_response(data, status_code):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(data),
        status=status_code
    )