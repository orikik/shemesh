from flask import request
from user.correct import Correct
from app import app

"""
@api {post} /registration New User Registration

@apiName GetUser
@apiGroup User

@apiParam {String} username Users name
@apiParam {String} password Users password
"""


@app.route('/registration', methods=['POST'])
def register():
    """Registers the user."""
    data = request.get_json()
    n = Correct().add(data)
    return n

