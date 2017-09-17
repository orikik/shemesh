from flask import request
from user.correct_data import Correct
from app import app


"""
@api {post} /update User update

@apiName UpdateUser
@apiGroup 1. User

@apiParam {String} cookie Users cookie(automatically)
@apiParam {String} [username] Users new name
@apiParam {String} [password] Users new password
"""


@app.route('/update', methods=['POST'])
def update():
    """Updating user data."""
    session = request.cookies.get('session')
    data = request.get_json()
    n = Correct().update(data, session)
    return n
