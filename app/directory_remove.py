from flask import request
from app import app
from user.new_user import User
from director.correct import Correct


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
    username = str(User().find_username(session))
    n = Correct().remove_dir(data=data, username=username)
    return n
