from user.correct import Correct
from flask import request
from app import app
from user.new_user import User

"""
@api {post, get} /remove User deletion

@apiName DelUser
@apiGroup User

@apiParam {Number} id Users unique ID
@apiParam {String} username Users name
@apiParam {String} password Users password

@apiSuccess {String} username Users name
"""


@app.route('/remove', methods=['POST'])
def remove_post():
    """Deleting a user."""
    data = request.get_json()
    n = Correct().remove(data)
    return n


@app.route('/remove', methods=['GET'])
def remove_get():
    """Deleting a user."""
    session = request.cookies.get('session')
    n = User().remove_user2(session=session)
    return n
