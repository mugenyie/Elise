import unittest
import os
import json
from flask import jsonify
from src.app import create_app, db

class accountsTest(unittest.TestCase):
  """
  accounts Test Case
  """
  def setUp(self):
    """
    Test Setup
    """
    self.app = create_app("testing")
    self.client = self.app.test_client()
    self.user = {
      'name': 'Emmanuel C. Mugenyi',
      'email': 'ecmugenyi@gmail.com',
      'password': '1234',
      'phonenumber': '256787744279'
    }

    with self.app.app_context():
      # create all tables
      db.create_all()
  
  def test_user_creation(self):
    """ test user creation with valid credentials """
    res = self.client.post('/api/v1/accounts/', headers={'Content-Type': 'application/json'}, data=json.dumps(self.user))
    json_data = res.get_json() #json.loads(res.data)
    self.assertTrue(json_data.get('auth_token'))
    self.assertEqual(res.status_code, 201)

  def test_user_creation_with_existing_email(self):
    """ test user creation with already existing email"""
    res = self.client.post('/api/v1/accounts/', headers={'Content-Type': 'application/json'}, data=json.dumps(self.user))
    self.assertEqual(res.status_code, 201)
    res = self.client.post('/api/v1/accounts/', headers={'Content-Type': 'application/json'}, data=json.dumps(self.user))
    json_data = res.get_json()
    self.assertEqual(res.status_code, 400)
    self.assertTrue(json_data.get('error'))

  def test_user_creation_with_no_password(self):
    """ test user creation with no password"""
    user1 = {
      'name': 'olawale',
      'email': 'olawale1@mail.com',
    }
    res = self.client.post('/api/v1/accounts/', headers={'Content-Type': 'application/json'}, data=json.dumps(user1))
    json_data = res.get_json()
    self.assertEqual(res.status_code, 400)
    self.assertTrue(json_data.get('password'))

  def test_user_creation_with_no_email(self):
    """ test user creation with no email """
    user1 = {
      'name': 'olawale',
      'pasword': 'olawale1@mail.com',
    }
    res = self.client.post('/api/v1/accounts/', headers={'Content-Type': 'application/json'}, data=json.dumps(user1))
    json_data = res.get_json()
    self.assertEqual(res.status_code, 400)
    self.assertTrue(json_data.get('email'))

  def test_user_creation_with_empty_request(self):
    """ test user creation with empty request """
    user1 = {}
    res = self.client.post('/api/v1/accounts/', headers={'Content-Type': 'application/json'}, data=json.dumps(user1))
    json_data = res.get_json()
    self.assertEqual(res.status_code, 400)
  
  def test_user_login(self):
    """ User Login Tests """
    res = self.client.post('/api/v1/accounts/', headers={'Content-Type': 'application/json'}, data=json.dumps(self.user))
    self.assertEqual(res.status_code, 201)
    res = self.client.post('/api/v1/accounts/login', headers={'Content-Type': 'application/json'}, data=json.dumps(self.user))
    json_data = res.get_json()
    self.assertTrue(json_data.get('auth_token'))
    self.assertEqual(res.status_code, 200)

  def test_user_login_with_invalid_password(self):
    """ User Login Tests with invalid credentials """
    user1 = {
      'password': 'olawale',
      'email': 'olawale@mail.com',
    }
    res = self.client.post('/api/v1/accounts/', headers={'Content-Type': 'application/json'}, data=json.dumps(self.user))
    self.assertEqual(res.status_code, 201)
    res = self.client.post('/api/v1/accounts/login', headers={'Content-Type': 'application/json'}, data=json.dumps(user1))
    json_data = res.get_json()
    self.assertFalse(json_data.get('auth_token'))
    self.assertEqual(json_data.get('error'), 'invalid credentials')
    self.assertEqual(res.status_code, 400)

  def test_user_login_with_invalid_email(self):
    """ User Login Tests with invalid credentials """
    user1 = {
      'password': 'passw0rd!',
      'email': 'olawale1111@mail.com',
    }
    res = self.client.post('/api/v1/accounts/', headers={'Content-Type': 'application/json'}, data=json.dumps(self.user))
    self.assertEqual(res.status_code, 201)
    res = self.client.post('/api/v1/accounts/login', headers={'Content-Type': 'application/json'}, data=json.dumps(user1))
    json_data = res.get_json()
    self.assertFalse(json_data.get('auth_token'))
    self.assertEqual(json_data.get('error'), 'invalid credentials')
    self.assertEqual(res.status_code, 400)

  def test_user_get_me(self):
    """ Test User Get Me """
    res = self.client.post('/api/v1/accounts/', headers={'Content-Type': 'application/json'}, data=json.dumps(self.user))
    self.assertEqual(res.status_code, 201)
    auth_token = res.get_json().get('auth_token')
    res = self.client.get('/api/v1/accounts/me', headers={'Content-Type': 'application/json', 'auth_token': auth_token})
    json_data = res.get_json()
    self.assertEqual(res.status_code, 200)
    self.assertEqual(json_data.get('email'), 'ecmugenyi@gmail.com')
    self.assertEqual(json_data.get('name'), 'Emmanuel C. Mugenyi')

  def test_user_update_me(self):
    """ Test User Update Me """
    user1 = {
      'name': 'new name'
    }
    res = self.client.post('/api/v1/accounts/', headers={'Content-Type': 'application/json'}, data=json.dumps(self.user))
    self.assertEqual(res.status_code, 201)
    auth_token = res.get_json().get('auth_token')
    res = self.client.put('/api/v1/accounts/me', headers={'Content-Type': 'application/json', 'auth_token': auth_token}, data=json.dumps(user1))
    json_data = res.get_json()
    self.assertEqual(res.status_code, 200)
    self.assertEqual(json_data.get('name'), 'new name')

  def test_delete_user(self):
    """ Test User Delete """
    res = self.client.post('/api/v1/accounts/', headers={'Content-Type': 'application/json'}, data=json.dumps(self.user))
    self.assertEqual(res.status_code, 201)
    auth_token = res.get_json().get('auth_token')
    res = self.client.delete('/api/v1/accounts/me', headers={'Content-Type': 'application/json', 'auth_token': auth_token})
    self.assertEqual(res.status_code, 204)
    
  def tearDown(self):
    """
    Tear Down
    """
    with self.app.app_context():
      db.session.remove()
      db.drop_all()

if __name__ == "__main__":
  unittest.main() 