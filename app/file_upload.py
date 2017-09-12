from device.correct_data import Correct
from flask import request
from app import app
from user.new_user import User


"""
@api {post} /upload  Upload the file

@apiName UploadFile
@apiGroup Files

@apiParam {Number} cookie User cookies after authorization(automatically)
@apiParam {String} [storage_path] A place where to save the file
@apiParam {String} my_path The path to the file
"""


@app.route('/upload', methods=['POST'])
def upload():
    data = request.get_json()
    session = request.cookies.get('session')
    username = str(User().find_username(session))
    n = Correct().add(data=data, username=username)
    return n
