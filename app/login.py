from flask import request, make_response
from app import app
from user.correct import Correct
import uuid

"""
@api {post, get} /login User login

@apiName LoginUser
@apiGroup User

@apiParam {Number} id Users unique ID
@apiParam {String} username Users name
@apiParam {String} password Users password

@apiSuccess {String} username Users name
@apiSuccess {String} cookie Users cookie
"""


@app.route('/login', methods=['POST'])
def login():
    """log the user in."""
    data = request.get_json()
    n = Correct().login(data)
    return n



