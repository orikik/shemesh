from device.correct_data import Correct
from flask import request
from app import app
from user.DB_user_func import User


"""
@api {post} /upload  Upload the file

@apiName UploadFile
@apiGroup 3. Files

@apiParam {Number} cookie User cookies after authorization(automatically)
@apiParam {String} [storage_path] A place where to save the file
@apiParam {String} my_path The path to the file
"""


@app.route('/upload', methods=['POST'])
def upload():
    """Upload user file."""
    data = request.get_json()
    session = request.cookies.get('session')
    username = User().find_username(session)
    if username:
        n = Correct().add(data=data, username=str(username))
        return n
    else:
        return 'You are not authorized', 401

