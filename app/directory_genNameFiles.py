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


@app.route('/get_dir', methods=['POST'])
def get_dir():
    """create new directory"""
    session = request.cookies.get('session')
    data = request.get_json()
    username = User().find_username(session)
    key1 = 'path' in data
    key2 = 'name' in data
    if key1 and key2 and len(data) == 2:
        f = Dir(username=username, path_to=data['path'], name=data['name']).getting_a_list_of_directory_files()
    elif key2 and len(data) == 1:
        f = Dir(username=username, name=data['name']).getting_a_list_of_directory_files()
    else:
        return 'Incorrect data'
    return f
