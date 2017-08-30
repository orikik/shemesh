from flask import request, make_response
from app import app
import mongo
import uuid
from new_user import User

"""
@api {post, get} /login User login

@apiName LoginUser
@apiGroup User

@apiParam {Number} id Users unique ID
@apiParam {String} username Users name
@apiParam {String} password Users password

@apiSuccess {String} username Users name
@apiSuccess {String} cookie Users cookie
"""


@app.route('/login', methods=['POST'])
def login():
    """log the user in."""
    data = request.get_json()
    user = User().user(data)
    if user:
        if mongo.collection.find_one({"username": user['username'], "password": user['password']}):
            resp = make_response('Login successful')
            uuid_user = uuid.uuid4().hex
            resp.set_cookie('session', uuid_user)
            mongo.collection.update({'username': user['username']}, {"$set": {"session": uuid_user}})

            return resp
        else:
            return make_response('Invalid username/password')
    else:
        return 'Incorrect data'
