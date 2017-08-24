from flask import request, make_response
from app import app
import mongo
import uuid


@app.route('/login', methods=['GET', 'POST'])
def login():
    """log the user in."""
    user = request.get_json()
    if mongo.collection.find({"username": user['username'], "password": user['password']}).count() > 0:
        resp = make_response('Login successful')
        uuidUser = uuid.uuid4().hex
        resp.set_cookie('session', uuidUser)
        mongo.collection.update({'username': user['username']}, {"$set": {"session": uuidUser}})

        return resp
        #return 'Login successful'
    else:
        return 'Invalid username/password'