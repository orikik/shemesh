from flask import request
from new_user import User
from app import app
import mongo


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Registers the user."""
    username = request.get_json()
    if mongo.collection.find({"username": username['username']}).count() == 0:
        mongo.collection.save(username)
        return 'A new account has been created. ' + \
               'Login: ' + username['username'] + ', ' +\
               'Password: ' + username['password']
    else:
        return 'Login is used.'


@app.route('/remove', methods=['GET', 'POST'])
def remove():
    """Deleting a user."""
    username = request.get_json()
    if mongo.collection.find({"username": username['username']}).count() > 0:
        mongo.collection.remove(username)
        return 'The user was deleted.'
    else:
        return 'User with such login does not exist.'


@app.route('/login', methods=['GET', 'POST'])
def login():
    """log the user in."""
    username = request.get_json()
    if mongo.collection.find({"username": username['username'], "password": username['password']}).count() == 1:
        return 'Login successful'
    else:
        return 'Invalid username/password'