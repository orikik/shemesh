from flask import request
from user.correct import Correct
from app import app

"""
@api {post} /register New User Registration

@apiName GetUser
@apiGroup User

@apiParam {Number} id Users unique ID
@apiParam {String} username Users name
@apiParam {String} password Users password

@apiSuccess {String} username Users name
@apiSuccess {String} password Users password
"""


@app.route('/register', methods=['POST'])
def register():
    """Registers the user."""
    data = request.get_json()
    n = Correct().add(data)
    return n

