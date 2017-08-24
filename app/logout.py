from flask import request, make_response
from app import app
import mongo
import uuid

"""
@api {get} /logout User logout

@apiName LogoutUser
@apiGroup User

@apiParam {String} cookie Users cookie
"""


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session = request.cookies.get('session')
    mongo.collection.update({'session': session}, {'$unset': {'session': 1}})
    resp = make_response("logout")
    resp.set_cookie('session', expires=0)
    return resp