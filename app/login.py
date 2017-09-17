from flask import request
from app import app
from user.DB_user_func import User
from user.correct_data import Correct


"""
@api {post} /login User login

@apiName LoginUser
@apiGroup 1. User

@apiParam {String} username Users name
@apiParam {String} password Users password

@apiSuccess {String} cookie Users cookie
"""


@app.route('/login', methods=['POST'])
def login():
    """log the user in."""
    data = request.get_json()
    session = request.cookies.get('session')
    if session:
        User().remove_user_cookie(session=session)
        n = Correct().login(data)
    else:
        n = Correct().login(data)
    return n



