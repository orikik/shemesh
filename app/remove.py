from user.correct_data import Correct
from flask import request
from app import app
from user.DB_user_func import User

"""
@api {post} /remove User deletion

@apiName DelUser1
@apiGroup 1. User

@apiParam {String} username Users name
@apiParam {String} password Users password
"""


@app.route('/remove', methods=['POST'])
def remove_post():
    """Deleting a user."""
    data = request.get_json()
    n = Correct().remove(data)
    return n

"""
@api {get} /remove User deletion

@apiName DelUser2
@apiGroup 1. User

@apiParam {String} cookie Users cookie(automatically)
"""

@app.route('/remove', methods=['GET'])
def remove_get():
    """Deleting a user."""
    session = request.cookies.get('session')
    n = User().remove_user2(session=session)
    return n
