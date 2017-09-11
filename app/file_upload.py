from device.correct_data import Correct
from flask import request
from app import app
from user.new_user import User


@app.route('/upload', methods=['POST'])
def upload():
    data = request.get_json()
    session = request.cookies.get('session')
    username = str(User().find_username(session))
    n = Correct().add(data=data, username=username)
    return n
