from flask import request
from user.correct import Correct
from app import app


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


@app.route('/update', methods=['POST'])
def update():
    """update"""
    session = request.cookies.get('session')
    data = request.get_json()
    n = Correct().update(data, session)
    return n
