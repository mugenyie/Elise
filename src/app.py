#src/app.py

from flask import Flask

from .config import app_config
from .shared.models import db, bcrypt

# import accounts blueprint
from .account.apiviews.AccountView import account_api as account_blueprint
from .account.apiviews.BusinessView import business_api as business_blueprint


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

  app.register_blueprint(account_blueprint, url_prefix='/api/v1/accounts')
  app.register_blueprint(business_blueprint, url_prefix='/api/v1/businesses')

  @app.route('/', methods=['GET'])
  def index():
    """
    initial endpoint
    """
    return 'Hello world! this is the future home of gobulk.co'
  
  return app