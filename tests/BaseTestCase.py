import unittest
import os
import json
from flask import jsonify
from src.app import create_app, db


class BaseTestCase(unittest.TestCase):
    """ Base Test Case"""
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

    def tearDown(self):
        """
        Tear Down
        """
        with self.app.app_context():
            db.session.remove()
            db.drop_all()