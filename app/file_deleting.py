from device.correct_data import Correct
from flask import request
from app import app
from user.new_user import User


@app.route('/delete_file', methods=['POST'])
def delete_file():
    data = request.get_json()
    session = request.cookies.get('session')
    username = str(User().find_username(session))
    n = Correct().remove(username=username, data=data)
    return n
