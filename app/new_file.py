import dev_choice
import shutil
from flask import request
from app import app
import mongo
from new_user import User

@app.route('/upload', methods=['POST'])
def upload():
    data = request.get_json()
    session = request.cookies.get('session')
    username = User().find_username(session)
    params_file = {
        'username': username,
        'path': data['path'],
        'file_format': '.txt'
    }
    mongo.file_collection.save(params_file)
    shutil.copy2(data['path'], dev_choice.path(username))
    return 'A new file added.'