from flask import request
from app import app
from directories.correct_data import Correct
from user.DB_user_func import User

"""
@api {post} /get_dir List of files in the directory

@apiName GetFilesDir
@apiGroup Directories

@apiParam {Number} cookie User cookies after authorization(automatically)
@apiParam {String} [path] Path to the directory
@apiParam {String} name The name of the directory
"""



@app.route('/get_dir', methods=['POST'])
def get_dir():
    """get list files from directory"""
    session = request.cookies.get('session')
    data = request.get_json()
    username = User().find_username(session)
    if username:
        n = Correct().get_list(data=data, username=str(username))
        return n
    else:
        return 'You are not authorized', 401
