#/src/views/UserView

from flask import request, json, Response, Blueprint, g, jsonify
from ...account.models.AccountModel import AccountModel, AccountSchema
from ...account.Authentication import Auth
from ...shared.apiviews import custom_response

account_api = Blueprint('account_api', __name__)
account_schema = AccountSchema()

@account_api.route('/', methods=['POST'])
def create():
  """
  Create Account Function
  """
  req_data = request.get_json()
  data, error = account_schema.load(req_data)

  if error:
    return custom_response(error, 400)
  
  # check if user already exist in the db
  user_email_in_db = AccountModel.get_user_by_email(data.get('email'))
  user_phone_in_db = AccountModel.get_user_by_phonenumber(data.get('phonenumber'))
  if user_email_in_db:
    message = {'error': 'User already exist, please supply another email address'}
    return custom_response(message, 400)
  if user_phone_in_db:
    message = {'error': 'User already exist, please supply another phone number'}
    return custom_response(message, 400)
  
  account = AccountModel(data)
  account.save()
  account_data = account_schema.dump(account).data
  token = Auth.generate_token(account_data.get('id'))
  return custom_response({'auth_token': token}, 201)

@account_api.route('/', methods=['GET'])
@Auth.auth_required
def get_all():
  """
  Get all accounts
  """
  accounts = AccountModel.get_all_users()
  account_data = account_schema.dump(accounts, many=True).data
  return custom_response(account_data, 200)

@account_api.route('/<string:account_id>', methods=['GET'])
@Auth.auth_required
def get_a_user(account_id):
  """
  Get a single user
  """
  account = AccountModel.get_one_user(account_id)
  if not account:
    return custom_response({'error': 'user not found'}, 404)
  
  account_data = account_schema.dump(account).data
  return custom_response(account_data, 200)

@account_api.route('/me', methods=['PUT'])
@Auth.auth_required
def update():
  """
  Update me
  """
  req_data = request.get_json()
  data, error = account_schema.load(req_data, partial=True)
  if error:
    return custom_response(error, 400)

  account = AccountModel.get_one_user(g.user.get('id'))
  account.update(data)
  account_data = account_schema.dump(account).data
  return custom_response(account_data, 200)

@account_api.route('/me', methods=['DELETE'])
@Auth.auth_required
def delete():
  """
  Delete a user
  """
  account = AccountModel.get_one_user(g.user.get('id'))
  account.delete()
  return custom_response({'message': 'deleted'}, 204)

@account_api.route('/me', methods=['GET'])
@Auth.auth_required
def get_me():
  """
  Get me
  """
  account = AccountModel.get_one_user(g.user.get('id'))
  account_data = account_schema.dump(account).data
  return custom_response(account_data, 200)


@account_api.route('/login', methods=['POST'])
def login():
  """
  User Login Function
  """
  req_data = request.get_json()

  data, error = account_schema.load(req_data, partial=True)
  if error:
    return custom_response(error, 400)
  if not data.get('email') or not data.get('password'):
    return custom_response({'error': 'you need email and password to sign in'}, 400)
  account = AccountModel.get_user_by_email(data.get('email'))
  if not account:
    return custom_response({'error': 'invalid credentials'}, 400)
  if not account.check_hash(data.get('password')):
    return custom_response({'error': 'invalid credentials'}, 400)
  account_data = account_schema.dump(account).data
  token = Auth.generate_token(account_data.get('id'))
  return custom_response({'auth_token': token}, 200)