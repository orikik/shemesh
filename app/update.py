from flask import request
from user.correct import Correct
from app import app


"""
@api {post} /update User update

@apiName UpdateUser
@apiGroup User

@apiParam {String} cookie Users cookie(automatically)
@apiParam {String} [username] Users new name
@apiParam {String} [password] Users new password
"""


@app.route('/update', methods=['POST'])
def update():
    """update"""
    session = request.cookies.get('session')
    data = request.get_json()
    n = Correct().update(data, session)
    return n
