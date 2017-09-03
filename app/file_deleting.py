from dev_choice import dev
from flask import request
from app import app
from new_user import User

@app.route('/delete_file', methods=['POST'])
def delete_file():
    data = request.get_json()
    session = request.cookies.get('session')
    username = User().find_username(session)
    n = dev().remove_file(username=username, name=data['name'])
    return n