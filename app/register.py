from flask import request
from app import app
import mongo


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Registers the user."""
    username = request.get_json()
    if mongo.collection.find({"username": username['username']}).count() == 0:
        mongo.collection.save(username)
        print("Set-cookie: name=value")
        print("Content-type: text/html\n")
        return 'A new account has been created. ' + \
               'Login: ' + username['username'] + ', ' +\
               'Password: ' + username['password']
    else:
        return 'Login is used.'
