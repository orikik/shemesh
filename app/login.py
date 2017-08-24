from flask import request
from app import app
import mongo


@app.route('/login', methods=['GET', 'POST'])
def login():
    """log the user in."""
    username = request.get_json()
    if mongo.collection.find({"username": username['username'], "password": username['password']}).count() > 0:
        return 'Login successful'
    else:
        return 'Invalid username/password'