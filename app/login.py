from flask import request, make_response
from app import app
import mongo
import uuid


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    """log the user in."""
    user = request.get_json()
    if mongo.collection.find_one({"username": user['username'], "password": user['password']}):
        resp = make_response('Login successful')
        uuid_user = uuid.uuid4().hex
        resp.set_cookie('session', uuid_user)
        mongo.collection.update({'username': user['username']}, {"$set": {"session": uuid_user}})

        return resp
    else:
        return make_response('Invalid username/password')
