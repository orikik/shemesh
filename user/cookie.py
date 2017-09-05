import uuid
from flask import make_response
from user.new_user import User

def get_cookie(username):
    resp = make_response('Login successful')
    uuid_user = uuid.uuid4().hex
    resp.set_cookie('session', uuid_user)
    User().update_user_cookie(username=username, cookie=uuid_user)
    return resp
