from flask import request, make_response
from app import app
import mongo


"""
@api {get, post} /logout User logout

@apiName LogoutUser
@apiGroup User

@apiParam {String} cookie Users cookie(automatically)
"""


@app.route('/logout', methods=['GET', 'POST'])
def logout_get():
    session = request.cookies.get('session')
    mongo.collection.update_one({'session': session}, {'$unset': {'session': 1}})
    resp = make_response("logout")
    resp.set_cookie('session', expires=0)
    return resp
