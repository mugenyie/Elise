# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from ...config import CustomConfigs

def send_mail(from_,to,subject,message):
    """send email through sendgridapi client"""
    message = Mail(
        from_email=from_,
        to_emails=to,
        subject=subject,
        html_content=message)
    sg = SendGridAPIClient(CustomConfigs.SENDGRID_API_KEY)
    response = sg.send(message)
    return response


    