from device.correct_data import Correct
from flask import request
from app import app
from user.new_user import User


"""
@api {post} /remove_file Delete the file

@apiName RemoveFile
@apiGroup Files

@apiParam {Number} cookie User cookies after authorization(automatically)
@apiParam {String} [storage_path] The place where you want to delete the file
@apiParam {String} name The name of the file
"""


@app.route('/remove_file', methods=['POST'])
def remove_file():
    data = request.get_json()
    session = request.cookies.get('session')
    username = str(User().find_username(session))
    n = Correct().remove(username=username, data=data)
    return n
