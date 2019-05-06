# /src/config.py

import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class Development:
    """
    Development environment configuration
    """
    DEBUG = True
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

class Production:
    """
    Production environment configurations
    """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

class Testing:
    """
    Development environment configuration
    """
    TESTING = True
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_TEST_URL') or "postgresql://elise:Elise1*@127.0.0.1:5432/elise_test_db"
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class CustomConfigs:
    #Africa's Talking
    AFRICASTALKING_PRODUCTION_BASEURL = 'https://api.africastalking.com'
    AFRICASTALKING_SANDBOX_BASEURL = 'https://api.sandbox.africastalking.com'
    AFRICASTALKING_API_KEY=os.getenv('AFRICASTALKING_API_KEY')
    AFRICASTALKING_PRODUCTION_APPNAME=os.getenv('AFRICASTALKING_PRODUCTION_APPNAME')
    AFRICASTALKING_PRODUCTION_USERNAME=os.getenv('AFRICASTALKING_PRODUCTION_USERNAME')
    AFRICASTALKING_SANDBOX_APPNAME=os.getenv('AFRICASTALKING_SANDBOX_APPNAME')
    AFRICASTALKING_SANDBOX_USERNAME=os.getenv('AFRICASTALKING_SANDBOX_USERNAME')
    #Sendgrid
    SENDGRID_API_KEY=os.getenv('SENDGRID_API_KEY')

app_config = {
    'development': Development,
    'production': Production,
    'testing': Testing
}