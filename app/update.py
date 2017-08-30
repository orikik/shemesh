from flask import request
from app import app
import mongo
from new_user import User


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
    user = User().user(data)
    if user:
        if mongo.collection.find_one({"session": session}):
            if not mongo.collection.find_one({"username": user['username']}):
                mongo.collection.update({'session': session}, {'$set': {"username": user['username']}})
                mongo.collection.update({'session': session}, {'$set': {"password": user['password']}})
                return 'New login: ' + user['username'] + ', ' + \
                       'New password: ' + user['password']
            else:
                return 'Login is used.'
        else:
            return 'You are not loged in.'
    else:
        return 'Incorrect data'
