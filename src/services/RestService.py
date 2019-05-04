"""
RestService is the python restclient for Elise Project
Sample Usage

restclient = RestClient("http://api.gobulk.co/v1")
restrequest = RestRequest(
    '/login/',
    'post'
)
restrequest.add_header('auth_token','iufoewbfowebfoewufbo')
restrequest.add_object(User(name="Tome",age=20))
restrequest.add_params("k",9)
restclient.execute(restrequest)

class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password
"""

import json, requests

class RestRequest:
    """new Rest Request"""
    def __init__(self, resource, method):
        self.resource = resource
        self.method = method
        self.headers = {'content-type': 'application/json'}
        self.params = {}
        self.payload = None
    def add_header(self, k, v):
        self.headers.update({k:v})
    def add_params(self, k, v):
        self.params.update({k:v})
    def add_object(self, object):
        self.payload = object.__dict__

class RestClient:
    """create new rest client"""
    def __init__(self, baseurl):
        self.baseurl = baseurl
    def execute(self,request):
        url = self.baseurl + request.resource
        payload = json.dumps(request.payload)
        headers = request.headers
        if request.method == "post":
            return requests.post(url, data=payload, headers=headers)
        if request.method == "get":
            return requests.get(url, params=request.params, headers=headers)
        if request.method == "put":
            return requests.put(url, data=payload, headers=headers)