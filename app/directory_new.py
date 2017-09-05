from flask import request
from app import app
from user.new_user import User
from director.correct import Correct


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


@app.route('/new_dir', methods=['POST'])
def new_dir():
    """create new directory"""
    session = request.cookies.get('session')
    data = request.get_json()
    username = User().find_username(session)
    n = Correct().add_dir(data=data, username=username)
    return n

