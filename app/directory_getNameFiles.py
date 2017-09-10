from flask import request
from app import app
from director.correct import Correct
from user.new_user import User

"""
@api {post, get} /update User update

@apiName UpdateUser
@apiGroup User

@apiParam {Number} id Users unique ID
@apiParam {String} username Users new name
@apiParam {String} password Users new password

@apiSuccess {String} username Users name
@apiSuccess {String} password Users new password
"""


@app.route('/get_dir', methods=['POST'])
def get_dir():
    """get list files from directory"""
    session = request.cookies.get('session')
    data = request.get_json()
    username = str(User().find_username(session))
    n = Correct().get_list(data=data, username=username)
    return n
