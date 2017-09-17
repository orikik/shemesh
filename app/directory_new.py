from flask import request
from app import app
from user.DB_user_func import User
from directories.correct_data import Correct


"""
@api {post} /new_dir Create a new directory

@apiName NewDir
@apiGroup 2. Directories

@apiParam {Number} cookie User cookies after authorization(automatically)
@apiParam {String} [path] The place where you want to create the directory
@apiParam {String} name The name of the directory
"""



@app.route('/new_dir', methods=['POST'])
def new_dir():
    """create new directory"""
    session = request.cookies.get('session')
    data = request.get_json()
    username = User().find_username(session)
    if username:
        n = Correct().add_dir(data=data, username=str(username))
        return n
    else:
        return 'You are not authorized', 401

