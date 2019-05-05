import json
from ...services.RestService import RestClient, RestRequest
from ...config import CustomConfigs

class AfricasTalkingService:
    """Make Calls to Africa's Talking API"""
    def __init__(self):
        self.client = RestClient(CustomConfigs.AFRICASTALKING_PRODUCTION_BASEURL)
        self.__apikey = CustomConfigs.AFRICASTALKING_API_KEY
        self.__username = CustomConfigs.AFRICASTALKING_PRODUCTION_USERNAME

    def generate_authtoken(self):
        """Generate new auth token"""
        request = RestRequest('/auth-token/generate','post')
        request.add_header('content-type','application/json')
        request.add_header('Accept', 'application/json')
        request.add_header('ApiKey', self.__apikey)
        request.add_body({
            "username": self.__username
        })
        response = self.client.execute(request)
        return response
        
    def send_sms(self, sms_body):
        """Send SMS"""
        request = RestRequest('/version1/messaging','post')
        request.add_header("Content-Type","application/x-www-form-urlencoded")
        request.add_header('ApiKey', self.__apikey)
        request.add_form_data(sms_body)
        response = self.client.execute(request)
        return response