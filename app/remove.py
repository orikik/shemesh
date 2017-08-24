from flask import request
from app import app
import mongo


@app.route('/remove', methods=['GET', 'POST'])
def remove():
    """Deleting a user."""
    username = request.get_json()
    if mongo.collection.find({"username": username['username']}).count() > 0:
        mongo.collection.remove(username)
        return 'The user was deleted.'
    else:
        return 'User with such login does not exist.'