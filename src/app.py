#src/app.py

from flask import Flask

from .config import app_config
from .shared.models import db, bcrypt

# import accounts blueprint
from .account.apiviews.AccountView import account_api as account_blueprint
from .account.apiviews.BusinessView import business_api as business_blueprint
from .products.messages.sms.apiview import sms_api as sms_blueprint
from .products.messages.whatsapp.apiview import whatsapp_api as whatsapp_blueprint
from .products.messages.email.apiview import email_api as email_blueprint


def create_app(env_name):
  """
  Create app
  """
  
  # app initiliazation
  app = Flask(__name__)

  app.config.from_object(app_config[env_name])

  # initializing bcrypt and db
  bcrypt.init_app(app)
  db.init_app(app)

  api_version = 'v1'
  app.register_blueprint(account_blueprint, url_prefix='/v1/accounts')
  app.register_blueprint(business_blueprint, url_prefix='/v1/businesses')
  app.register_blueprint(sms_blueprint, url_prefix='/v1/messages/sms')
  app.register_blueprint(whatsapp_blueprint, url_prefix='/v1/messages/whatsapp')
  app.register_blueprint(email_blueprint, url_prefix='/v1/messages/email')

  @app.route('/', methods=['GET'])
  def index():
    """
    initial endpoint
    """
    return 'Hello world! this is the future home of gobulk.co'
  
  return app