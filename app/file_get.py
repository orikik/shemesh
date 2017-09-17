from device.correct_data import Correct
from flask import request
from app import app
from user.DB_user_func import User


"""
@api {post} /get_file  Getting the file

@apiName GetFile
@apiGroup 3. Files

@apiParam {Number} cookie User cookies after authorization(automatically)
@apiParam {String} [storage_path] The place from where you want to get the file
@apiParam {String} my_path A place where to save the file
@apiParam {String} name The name of the file
"""


@app.route('/file_get', methods=['POST'])
def file_get():
    """download user file"""
    data = request.get_json()
    session = request.cookies.get('session')
    username = User().find_username(session)
    if username:
        n = Correct().get(data=data, username=str(username))
        return n
    else:
        return 'You are not authorized', 401
