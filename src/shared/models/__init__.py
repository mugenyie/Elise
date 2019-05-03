#src/shared/models/__init__.py

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# initialize our db
db = SQLAlchemy()
bcrypt = Bcrypt()


from ...account.models.AccountModel import AccountModel, AccountSchema
from ...account.models.BusinessModel import BusinessModel, BusinessSchema