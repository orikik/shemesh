from dev_choice import dev
from flask import request
from app import app
from new_user import User


@app.route('/upload', methods=['POST'])
def upload():
    data = request.get_json()
    session = request.cookies.get('session')
    username = User().find_username(session)
    n = dev().user_path(data=data, username=username)
    return n