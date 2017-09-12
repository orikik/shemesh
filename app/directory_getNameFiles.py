from flask import request
from app import app
from director.correct import Correct
from user.new_user import User

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
    username = str(User().find_username(session))
    n = Correct().get_list(data=data, username=username)
    return n
