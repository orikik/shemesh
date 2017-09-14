from device.correct_data import Correct
from flask import request
from app import app
from user.DB_user_func import User


"""
@api {post} /file_update  Update the file

@apiName UpdateFile
@apiGroup Files

@apiParam {Number} cookie User cookies after authorization(automatically)
@apiParam {String} [storage_path] The place from where you want to get the file
@apiParam {String} my_path The path to the file
"""


@app.route('/file_update', methods=['POST'])
def file_update():
    """Update the user file."""
    data = request.get_json()
    session = request.cookies.get('session')
    username = User().find_username(session)
    if username:
        n = Correct().update(data=data, username=str(username))
        return n
    else:
        return 'You are not authorized', 401
