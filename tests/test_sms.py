from .BaseTestCase import BaseTestCase
from src.providers.africastalking.SMSModel import SMSModel

class smsTest(BaseTestCase):
    def test_send_sms(self):
        sms = SMSModel(
            username = "check"
        )
        self.assertTrue(sms.send_sms())