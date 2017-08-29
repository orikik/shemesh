from flask import request
from app import app
import mongo


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
    user = request.get_json()
    if mongo.collection.find_one({"username": user['username'], "password": user['password']}):
        mongo.collection.remove(user)
        return 'The user was deleted.'
    else:
        return 'Wrong password or user with such login does not exist.'


@app.route('/remove', methods=['GET'])
def remove_get():
    """Deleting a user."""
    session = request.cookies.get('session')
    if mongo.collection.find_one({'session': session}):
        mongo.collection.remove({'session': session})
        return 'The user was deleted.'
    else:
        return 'You are not authorisate.'
