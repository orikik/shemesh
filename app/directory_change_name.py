from flask import request
from app import app
from user.new_user import User
from director.correct import Correct


"""
@api {post} /new_name_dir Change the name of the directory

@apiName ChangeDir
@apiGroup Directories

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
    username = str(User().find_username(session))
    n = Correct().change_name(data=data, username=username)
    return n
