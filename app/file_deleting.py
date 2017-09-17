from device.correct_data import Correct
from flask import request
from app import app
from user.DB_user_func import User


"""
@api {post} /remove_file Delete the file

@apiName RemoveFile
@apiGroup 3. Files

@apiParam {Number} cookie User cookies after authorization(automatically)
@apiParam {String} [storage_path] The place where you want to delete the file
@apiParam {String} name The name of the file
"""


@app.route('/remove_file', methods=['POST'])
def remove_file():
    """Delete the user file."""
    data = request.get_json()
    session = request.cookies.get('session')
    username = User().find_username(session)
    if username:
        n = Correct().remove(username=str(username), data=data)
        return n
    else:
        return 'You are not authorized', 401
