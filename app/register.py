from flask import request
from app import app
import mongo

"""
@api {get} /register sfsf sfsdf sdf sf 
@apiName GetUser
@apiGroup User

@apiParam {Number} id Users unique ID.

@apiSuccess {String} firstname Firstname of the User.
@apiSuccess {String} lastname  Lastname of the User.
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
