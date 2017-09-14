from flask import request, make_response
from app import app
from user.DB_user_func import User

"""
@api {get, post} /logout User logout

@apiName LogoutUser
@apiGroup User

@apiParam {String} cookie Users cookie(automatically)
"""


@app.route('/logout', methods=['GET', 'POST'])
def logout_get():
    """log the user out."""
    session = request.cookies.get('session')
    User().remove_user_cookie(session=session)
    resp = make_response("logout")
    resp.set_cookie('session', expires=0)
    return resp
