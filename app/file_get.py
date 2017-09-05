from device.correct_data import Correct
from flask import request
from app import app
from user.new_user import User


@app.route('/file_get', methods=['POST'])
def file_get():
    data = request.get_json()
    session = request.cookies.get('session')
    username = User().find_username(session)
    n = Correct().get(data=data, username=username)
    return n
