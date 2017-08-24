from flask import request
from app import app
import mongo

"""
@api {post, get} /register New User Registration

@apiName GetUser
@apiGroup User

@apiParam {Number} id Users unique ID
@apiParam {String} username Users name
@apiParam {String} password Users password

@apiSuccess {String} username Users name
@apiSuccess {String} password Users password
"""
@app.route('/register', methods=['GET', 'POST'])
def register():
    """Registers the user."""
    username = request.get_json()
    if mongo.collection.find({"username": username['username']}).count() == 0:
        mongo.collection.save(username)
        mongo.collection.update({}, {"$set": {"create": None},
                                     "$set": {"end": None}})
        print("Set-cookie: name=value")
        print("Content-type: text/html\n")
        return 'A new account has been created. ' + \
               'Login: ' + username['username'] + ', ' +\
               'Password: ' + username['password']
    else:
        return 'Login is used.'
