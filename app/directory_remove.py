from flask import request
from app import app
from user.DB_user_func import User
from directories.correct_data import Correct


"""
@api {post} /remove_dir Removing directory

@apiName RemoveDir
@apiGroup Directories

@apiParam {Number} cookie User cookies after authorization(automatically)
@apiParam {String} [path] The place where you want to remove the directory
@apiParam {String} name The name of the directory
"""


@app.route('/remove_dir', methods=['POST'])
def remove_dir():
    """create new directory"""
    session = request.cookies.get('session')
    data = request.get_json()
    username = User().find_username(session)
    if username:
        n = Correct().remove_dir(data=data, username=str(username))
        return n
    else:
        return 'You are not authorized', 401


