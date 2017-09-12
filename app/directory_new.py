from flask import request
from app import app
from user.new_user import User
from director.correct import Correct


"""
@api {post} /new_dir Create a new directory

@apiName NewDir
@apiGroup Directories

@apiParam {Number} cookie User cookies after authorization(automatically)
@apiParam {String} [path] The place where you want to create the directory
@apiParam {String} name The name of the directory
"""



@app.route('/new_dir', methods=['POST'])
def new_dir():
    """create new directory"""
    session = request.cookies.get('session')
    data = request.get_json()
    username = str(User().find_username(session))
    n = Correct().add_dir(data=data, username=username)
    return n

