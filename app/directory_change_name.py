from flask import request
from app import app
from user.DB_user_func import User
from directories.correct_data import Correct


"""
@api {post} /new_name_dir Change the name of the directory

@apiName ChangeDir
@apiGroup 2. Directories

@apiParam {Number} cookie User cookies after authorization(automatically)
@apiParam {String} [path] The place where you want to change the directory name
@apiParam {String} old_name The name of the directory you want to change
@apiParam {String} new_name New directory name
"""


@app.route('/new_name_dir', methods=['POST'])
def new_name_dir():
    """Change name directory"""
    session = request.cookies.get('session')
    data = request.get_json()
    username = User().find_username(session)
    if username:
        n = Correct().change_name(data=data, username=str(username))
        return n
    else:
        return 'You are not authorized', 401

