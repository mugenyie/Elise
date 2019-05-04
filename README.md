# Project Elise

[![Build Status](https://travis-ci.com/mugenyie/Elise.svg?token=9j5hSxhjhoLyxg2QAJKd&branch=develop)](https://travis-ci.com/mugenyie/Elise)

# User Account API
Create Account - POST api/v1/accounts/
{
	"username":"",
	"name":"",
	"email":"",
	"password":"",
	"phonenumber":""
}
Login User - POST api/v1/users/login
{
	"email":"",
	"password":""
}
Get A User Info - GET api/v1/accounts/<string:account_id>
Get All users - GET api/v1/accounts
Get My Info - GET api/v1/accounts/me
Edit My Info - PUT api/v1/accounts/me
DELETE My Account - DELETE api/v1/accounts/me

# Businesses API
Create a Business - POST api/v1/businesses/
{
	"name":"gobulk",
	"industry":"Software",
	"description":"Go bulk go smart"
}
Get All Businesses - GET api/v1/businesses
Get A Blogposts - GET api/v1/businesses/<string:business_id>
Update A Blogpost - PUT api/v1/business/<string:business_id>
Delete A Blogpost - DELETE api/v1/businesses/<string:business_id>