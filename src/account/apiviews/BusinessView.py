#/src/views/BusinessView.py
from flask import request, g, Blueprint, json, Response
from ..models.BusinessModel import BusinessModel, BusinessSchema
from ...account.Authentication import Auth
from ...shared.apiviews import custom_response

business_api = Blueprint('business_api', __name__)
business_schema = BusinessSchema()

@business_api.route('/', methods=['POST'])
@Auth.auth_required
def create():
  """
  Create Business Function
  """
  req_data = request.get_json()
  req_data['owner_id'] = g.user.get('id')
  data, error = business_schema.load(req_data)
  if error:
    return custom_response(error, 400)
  business = BusinessModel(data)
  business.save()
  data = business_schema.dump(business).data
  return custom_response(data, 201)

@business_api.route('/', methods=['GET'])
def get_all():
  """
  Get All Businesses
  """
  businesses = BusinessModel.get_all_businesses()
  data = business_schema.dump(businesses, many=True).data
  return custom_response(data, 200)

@business_api.route('/<string:business_id>', methods=['GET'])
def get_one(business_id):
  """
  Get A Business
  """
  business = BusinessModel.get_one_business(business_id)
  if not business:
    return custom_response({'error': 'business not found'}, 404)
  data = business_schema.dump(business).data
  return custom_response(data, 200)

@business_api.route('/<string:business_id>', methods=['PUT'])
@Auth.auth_required
def update(business_id):
  """
  Update A Business
  """
  req_data = request.get_json()
  business = BusinessModel.get_one_business(business_id)
  if not business:
    return custom_response({'error': 'post not found'}, 404)
  data = business_schema.dump(business).data
  if data.get('owner_id') != g.user.get('id'):
    return custom_response({'error': 'permission denied'}, 400)
  
  data, error = business_schema.load(req_data, partial=True)
  if error:
    return custom_response(error, 400)
  business.update(data)
  
  data = business_schema.dump(business).data
  return custom_response(data, 200)

@business_api.route('/<string:business_id>', methods=['DELETE'])
@Auth.auth_required
def delete(business_id):
  """
  Delete A Business
  """
  business = BusinessModel.get_one_business(business_id)
  if not business:
    return custom_response({'error': 'post not found'}, 404)
  data = business_schema.dump(business).data
  if data.get('owner_id') != g.user.get('id'):
    return custom_response({'error': 'permission denied'}, 400)

  business.delete()
  return custom_response({'message': 'deleted'}, 204)