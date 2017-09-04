from flask import request

from app import app
from devicee.correct_data import Correct
from new_user import User


@app.route('/file_update', methods=['POST'])
def file_update():
    data = request.get_json()
    session = request.cookies.get('session')
    username = User().find_username(session)
    n = Correct().update(data=data, username=username)
    return n
