import os
from flask import request, make_response
from app import app
import mongo
from new_user import User

"""
@api {post, get} /remove User deletion

@apiName DelUser
@apiGroup User

@apiParam {Number} id Users unique ID
@apiParam {String} username Users name
@apiParam {String} password Users password

@apiSuccess {String} username Users name
"""


@app.route('/remove', methods=['POST'])
def remove_post():
    """Deleting a user."""
    data = request.get_json()
    user = User().user(data)
    if user:
        if mongo.collection.find_one({"username": user['username'], "password": user['password']}):
            mongo.collection.remove(user)
            os.rmdir(path='C:/test_server/' + user['username'])
            return 'The user was deleted.'
        else:
            return 'Wrong password or user with such login does not exist.'
    else:
        return 'Incorrect data'


@app.route('/remove', methods=['GET'])
def remove_get():
    """Deleting a user."""
    session = request.cookies.get('session')
    if mongo.collection.find_one({'session': session}):
        mongo.collection.remove({'session': session})
        resp = make_response("remove")
        resp.set_cookie('session', expires=0)
        return 'The user was deleted.'
    else:
        return 'You are not authorisate.'
