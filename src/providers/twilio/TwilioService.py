from twilio.rest import Client 


class TwilioService:
    """Twilio Elise Service"""
    def __init__(self):
        self.__account_sid = 'AC38f252135563cd9ddf0e53e0797e858f' 
        self.__auth_token = '2d192be2a7e1669632720b6f39b16c0d' 
        self.__client = Client(self.__account_sid, self.__auth_token)
        
    def send_whatsapp(self, to, message):
        """Send whatsapp message"""
        __from_ = 'whatsapp:+14155238886'
        __body = message
        __to = 'whatsapp:+' + to
        response = self.__client.messages.create(
            from_ = __from_,  
            body = __body,      
            to = __to
        )
        return response.sid
    
    def send_sms(self, from_, to, message, callback):
        message = self.__client.messages.create(
            body=message,
            from_='+'+from_,
            status_callback=callback,
            to='+'+to
        )
        return message.sid

    def send_voice(self, from_,to,voice_url ):
        call = client.calls.create(
            url=voice_url,
            to='+'+to,
            from_='+'+from_
        )
        return call.sid