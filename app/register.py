import os
from flask import request
from app import app
import mongo
from new_user import User
from dev_choice import dev
"""
@api {post} /register New User Registration

@apiName GetUser
@apiGroup User

@apiParam {Number} id Users unique ID
@apiParam {String} username Users name
@apiParam {String} password Users password

@apiSuccess {String} username Users name
@apiSuccess {String} password Users password
"""


@app.route('/register', methods=['POST'])
def register():
    """Registers the user."""
    data = request.get_json()
    user = User().params_user(data) #Validation of entered data
    if user:
        if not mongo.collection.find_one({"username": user['username']}):
            mongo.collection.save(user)
            print("Set-cookie: name=value")
            print("Content-type: text/html\n")
            return 'A new account has been created. ' + \
                   'Login: ' + user['username'] + ', ' + \
                   'Password: ' + user['password']
        else:
            return 'Login is used.'
    else:
        return 'Incorrect data'

