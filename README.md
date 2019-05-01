# Project Elise

[![Build Status](https://travis-ci.com/mugenyie/Elise.svg?token=9j5hSxhjhoLyxg2QAJKd&branch=develop)](https://travis-ci.com/mugenyie/Elise)

# User Account API

Create User - POST api/v1/users
Login User - POST api/v1/users/login
Get A User Info - GET api/v1/users/<int:user_id>
Get All users - GET api/v1/users
Get My Info - GET api/v1/users/me
Edit My Info - PUT api/v1/users/me
DELETE My Account - DELETE api/v1/users/me

# Transactions API

Create a Blogpost - POST api/v1/blogposts
Get All Blogposts - GET api/v1/blogposts
Get A Blogposts - GET api/v1/blogposts/<int:blogpost_id>
Update A Blogpost - PUT api/v1/blogposts/<int:blogpost_id>
Delete A Blogpost - DELETE api/v1/blogposts/<int:blogpost_id>