from flask import request
from app import app
from directorys import Dir
from new_user import User


"""
@api {post, get} /update User update

@apiName UpdateUser
@apiGroup User

@apiParam {Number} id Users unique ID
@apiParam {String} username Users new name
@apiParam {String} password Users new password

@apiSuccess {String} username Users name
@apiSuccess {String} password Users new password
"""


@app.route('/new_name_dir', methods=['POST'])
def new_name_dir():
    """create new directory"""
    session = request.cookies.get('session')
    data = request.get_json()
    username = User().find_username(session)
    key1 = 'old name' in data
    key2 = 'new name' in data
    key3 = 'path' in data
    if key1 and key2 and key3 and len(data) == 3:
        f = Dir(username=username, path_to=data['path'], name=data['old name']).change_name_directory(data['new name'])
    elif key1 and key2 and len(data) == 2:
        f = Dir(username=username, name=data['name']).change_name_directory(data['new name'])
    else:
        return 'Incorrect data'
    return f
